from tkinter.filedialog import *
from tkinter import messagebox
from os.path import expanduser
import selector
import random
from freqlist import FREQLIST
from database import DATABASE
from dict import DICT
import card
import datetime

TEST_SIZE = 100
MAX_RANK = 15000

MEAN_VAL = None
PR = None

WORDS_TO_LEARN = None

INDEX = None
LEN = None
WORDS = None

TO_LEARN = None


def survey(words, to_learn):
    global MEAN_VAL, PR, INDEX, LEN, WORDS_TO_LEARN, WORDS, TO_LEARN

    filemenu.entryconfig("Open", state="disabled")
    filemenu.entryconfig("Test vocabulary", state="disabled")
    filemenu.entryconfig("Clear info about user", state="disabled")
    filemenu.entryconfig("Estimate vocabulary size", state="disabled")
    btn_easy['state'] = 'normal'
    btn_hard['state'] = 'normal'

    MEAN_VAL = selector.get_mean_val(fl=FREQLIST)
    PR = selector.get_pr_func()

    WORDS_TO_LEARN = []

    WORDS = words
    INDEX = -1
    LEN = len(WORDS)

    TO_LEARN = to_learn

    next_word()


def next_word():
    global MEAN_VAL, PR, INDEX, LEN, WORDS, TO_LEARN, WORDS_TO_LEARN

    INDEX += 1

    if INDEX < LEN:
        word = WORDS[INDEX]
        corr = DICT.correct(word)
        if corr is None:
            corr = word
        WORD_STR.set(corr)
        STAT_STR.set("%d/%d" % (INDEX + 1, LEN))
        WORDINFO_STR.set(
                "rank = %d, p = %f, frequency = %f, value = %f" %
                (FREQLIST.rank(word), PR(word), FREQLIST.freq(word), MEAN_VAL(word)))
    else:
        WORD_STR.set('')
        STAT_STR.set('')
        WORDINFO_STR.set('')

        filemenu.entryconfig("Open", state="normal")
        filemenu.entryconfig("Test vocabulary", state="normal")
        filemenu.entryconfig("Clear info about user", state="normal")
        filemenu.entryconfig("Estimate vocabulary size", state="normal")
        btn_easy['state'] = 'disabled'
        btn_hard['state'] = 'disabled'

        if WORDS_TO_LEARN:
            homedir = expanduser("~")
            initialfile = datetime.datetime.now().strftime("%d-%m-%y %H-%M") + '.apkg'
            filename = asksaveasfilename(initialfile=initialfile, initialdir=homedir + "/Desktop", title="Save APKG file",
                                         filetypes=(("Anki files", "*.apkg"),), defaultextension='.apkg',)
            if filename:
                card.write_apkg(WORDS_TO_LEARN, filename)
                for word in WORDS_TO_LEARN:
                    DATABASE.modify_word(word, FREQLIST.rank(word), False, True)
        elif TO_LEARN:
            messagebox.showinfo("", "All words are known.")


def random_unknown_word(x, y, max_a):
    a = 0
    word = None
    while max_a is None or a < max_a:
        rank = random.randint(x, y - 1)
        word = FREQLIST.word(rank)
        if not DATABASE.exists(word) and DICT.exists(word):
            break
        else:
            word = None
        a += 1
    return word


def test_vocab():
    step = MAX_RANK // TEST_SIZE

    words = []
    i = 0
    while i < TEST_SIZE:
        word = random_unknown_word(i * step, (i + 1) * step, 50)
        if word is None:
            word = random_unknown_word(0, MAX_RANK + 1, None)
        words.append(word)
        i += 1

    survey(words, False)


def openfile():
    homedir = expanduser("~")
    filename = askopenfilename(initialdir=homedir + "/Desktop", title="Choose text file")
    if filename:
        with open(filename, 'r') as fh:
            words = selector.select(fh)
            survey(words, True)


def hard_clicked():
    if 0 <= INDEX < LEN:
        word = WORDS[INDEX]
        DATABASE.modify_word(word, FREQLIST.rank(word), False, False)
        if TO_LEARN and DICT.correct(word) is not None:
            WORDS_TO_LEARN.append(word)
    next_word()


def easy_clicked():
    if 0 <= INDEX < LEN:
        word = WORDS[INDEX]
        DATABASE.modify_word(word, FREQLIST.rank(word), True, True)
    next_word()


def clear_db():
    ans = messagebox.askyesno("", "Are you sure you want to clear info about user?")
    if ans:
        DATABASE.clear()


def estimate_vocab():
    pr = selector.get_pr_func()
    s = 0.0
    for i in range(0, 50000):
        word = FREQLIST.word(i)
        p = pr(word)
        s += p
    messagebox.showinfo("", "Estimated vocabulary size: %d" % (int(s)//3,))

root = Tk()
root.wm_title("Words")
root.geometry("480x320")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Test vocabulary", command=test_vocab)
filemenu.add_command(label="Clear info about user", command=clear_db)
filemenu.add_command(label="Estimate vocabulary size", command=estimate_vocab)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

WORD_STR = StringVar()
STAT_STR = StringVar()
WORDINFO_STR = StringVar()

lab_stat = Label(root, textvariable=STAT_STR)
lab_stat.grid(row=0, column=1, sticky=E)
lab_wordinfo = Label(root, textvariable=WORDINFO_STR)
lab_wordinfo.grid(row=0, column=0, sticky=W)

center_frame = Frame(root)
center_frame.grid(row=1, column=0, columnspan=2, sticky=N + S + W + E)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
lab_word = Label(center_frame, textvariable=WORD_STR, font="-size 18")
lab_word.place(relx=0.5, rely=0.5, anchor=CENTER)

bottom_frame = Frame(root)
bottom_frame.grid(row=2, column=0, columnspan=2)

btn_hard = Button(bottom_frame, text="Hard", command=hard_clicked, state="disabled", width=8)
btn_hard.pack(side=LEFT, padx=5, pady=5)
btn_easy = Button(bottom_frame, text="Easy", command=easy_clicked, state="disabled", width=8)
btn_easy.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()

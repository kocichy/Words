from database import DATABASE
import myparser
import freqlist
from dict import DICT
from math import log, fabs, exp

MAX = 12000
STEP = 1000
EPS = 0.01


def get_pr_func(db=DATABASE, max_=MAX, step=STEP):
    '''
    Zwraca funkcję, która przyporządokwuje ang. słowu szacowane prawdopodobieństwo znania tego słowa.

    :param db: baza danych zawierająca informacje o słownictwie użytkownika
    :param max_: maks. pozycja na liście frekwencyjnej słów branych pod uwagę
    :param step: dł. przedziału, na jakim jest szacowane prawdopodobieństwo
    :return: funkcja, która przyporządokwuje ang. słowu szacowane prawdopodobieństwo znania tego słowa
    '''
    rank_prob = [(-step // 2, 1.0)]
    rank = 0
    while rank + step <= max_:
        pr = db.known_words(rank, rank + step)
        mean_rank = rank + step // 2
        if pr is None:
            (r, p) = rank_prob[-1]
            pr = abs(r) / mean_rank * p
        rank_prob.append((mean_rank, pr))
        rank += step

    def pr_func(word):
        x = freqlist.FREQLIST.rank(word)
        if x is None:
            return EPS
        i = 0
        while i+1 < len(rank_prob):
            if rank_prob[i][0] <= x < rank_prob[i+1][0]:
                break
            i += 1
        if i+1 == len(rank_prob):
            (r, p) = rank_prob[-1]
            pr = abs(r) / x * p
            return pr
        (x1, y1) = rank_prob[i]
        (x2, y2) = rank_prob[i+1]
        return y1 + (y2 - y1) / (x2 - x1) * (x - x1)

    return pr_func


def get_utility_func(db=DATABASE, fl=freqlist.FREQLIST):
    '''
    Zwraca funkcję użyteczności, która przyporządkowuje słowu jego wartość.

    :param db: baza danych zawierająca informacje o słownictwie użytkownika
    :param fl: lista frekwencyjna
    :return: funkcja użyteczności, która przyporządkowuje słowu jego wartość
    '''
    pr = get_pr_func(db=db)
    C = 11.2

    def utility_func(word):
        f = fl.freq(word)
        p = 1.0 - pr(word)
        # print((word, f, p))
        return (log(C+f) - log(C)) * exp(C*p)

    return utility_func


def select(stream, db=DATABASE):
    '''
    Zwraca listę słów posortowanych według wartości funkcji użyteczności dla podanego strumienia znakowego.

    :param stream: strumień znakowy
    :param db: baza danych zawierająca informacje o słownictwie użytkownika
    :return: lista słów posortowanych według wartości funkcji użyteczności
    '''
    words = myparser.parse(stream)
    temp_fl = freqlist.FreqList()
    temp_fl.load(stream=stream)
    fl = freqlist.DynMixedFreqList([(freqlist.FREQLIST, 0.5), (temp_fl, 0.5)])
    utility_fun = get_utility_func(db=db, fl=fl)
    pr = get_pr_func(db=db)
    mean_word = []
    for word in words:
        if DICT.correct(word) is not None and DATABASE.known_now(word) == False:
            mean_word.append((utility_fun(word), word, pr(word), ))
    mean_word.sort(reverse=True)
    # print(mean_word)
    return [word for (_, word, _) in mean_word]

if __name__ == '__main__':
    pass

import pickle


class FreqList:
    '''
    Klasa opisuje listę frekwencyjną.
    '''
    def __init__(self, filename=None, stream=None):
        '''
        Tworzy listę frekwenycjną z pliku korzystając z pickle.load() lub samemu zliczając słowa w strumieniu.

        :param filename: plik .p (pickle), gdzie znajduje się opis listy frekwencyjnej
        :param stream: strumień znaków, jeśli filename to None, wtedy lista frekwencyjna jest tworzona ze strumienia
        :return:
        '''
        if filename is not None:
            self.words, self.word_freq, self.word_rank = pickle.load(open(filename, 'rb'))
        elif stream is not None:
            self.words = list()
            self.word_freq = dict()
            self.word_rank = dict()

            from myparser import tokens, normalize

            cnt = 0
            for token in tokens(stream):
                word = normalize(token)
                f = FREQLIST.freq(word)
                if f is not None and f > 0:
                    self.word_freq[word] = 1 + self.word_freq.get(word, 0)
                    cnt += 1

            freq_word = [(f, w) for (w, f) in self.word_freq.items()]
            freq_word.sort(reverse=True)

            for (_, word) in freq_word:
                self.word_freq[word] /= cnt
                self.word_rank[word] = len(self.words)
                self.words.append(word)
        else:
            self.words, self.word_freq, self.word_rank = list(), dict(), dict()

    def freq(self, word):
        '''
        Zwraca częstość słowa.

        :param word: słowo angielskie
        :return: częstość słowa
        '''
        return self.word_freq.get(word, None)

    def rank(self, word):
        '''
        Zwraca pozycję słowa na liście frekwencyjnej.

        :param word: ang. słowo
        :return: pozycja na liście frekwencyjnej
        '''
        return self.word_rank.get(word, None)

    def word(self, rank):
        '''
        Zwraca słowo na liście frekwencyjnej o podanej pozycji.

        :param rank: pozycja na liście frekwencyjnej
        :return: słowo
        '''
        if rank >= len(self.words):
            return None
        return self.words[rank]

    def dump(self, filename):
        '''
        Zapisuje listę frekwencyjną do plik *.p

        :param filename: nazwa pliku
        :return: None
        '''
        pickle.dump((self.words, self.word_freq, self.word_rank), open(filename, 'wb'))


class PGFreqList(FreqList):
    '''
    Lista frekwenycjna powstała dzięki Projektowi Gutenberg\n
    https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000\n
    https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/10001-20000\n
    https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/20001-30000\n
    https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/30001-40000\n
    \n
    Uwaga: Brak słowa o pozycji 2781.
    '''
    def __init__(self):
        self.words = []
        self.word_freq = dict()
        self.word_rank = dict()

        fh = open('freqlists/pg.list', 'r')
        rank = 0
        while True:
            line = fh.readline()
            if len(line) == 0:
                break
            row = line.split()
            word = row[1].lower()
            self.words.append(word)
            self.word_freq[word] = float(row[2]) / 1000000000.0
            self.word_rank[word] = rank
            rank += 1


class OSFreqList(FreqList):
    '''
    Lista frekwencyjna powstała dzięki OpenSubtitles.org\n
    https://invokeit.wordpress.com/frequency-word-lists/\n
    \n
    Total files: 23406\n
    Unique word count: 521426\n
    Total word count: 145376051\n
    Overall word count: 193225723
    '''
    def __init__(self):
        self.words = []
        self.word_freq = dict()
        self.word_rank = dict()

        fh = open('freqlists/opensubtitles.list', 'r', encoding='utf8')
        rank = 0
        sum_ = 0
        word_cnt_rank = []
        while True:
            line = fh.readline()
            if len(line) == 0:
                break
            row = line.split()
            word = row[0]
            cnt = int(row[1])
            sum_ += cnt
            word_cnt_rank.append((word, cnt, rank))
            rank += 1

        for (word, cnt, rank) in word_cnt_rank:
            self.words.append(word)
            self.word_freq[word] = cnt / sum_
            self.word_rank[word] = rank


class NGSLFreqList(FreqList):
    '''
    Lista frekwencyjna powstała z danych użytych do tworzenia New General Service List\n
    http://www.newgeneralservicelist.org/\n
    NGSL Stats & Frequencies to 34k
    '''
    def __init__(self):
        self.words = []
        self.word_freq = dict()
        self.word_rank = dict()

        fh = open('freqlists/ngsl.list', 'r', encoding='utf8')
        rank = 0
        while True:
            line = fh.readline()
            if len(line) == 0:
                break
            row = line.split()
            word = row[0].lower()
            self.words.append(word)
            self.word_freq[word] = float(row[1])
            self.word_rank[word] = rank
            rank += 1


class SpokenFreqList(FreqList):
    '''
    Lista frekwencyjna powstała z danych użytych do tworzenia New General Service List (język mówiony)\n
    http://www.newgeneralservicelist.org/\n
    NGSL Spoken Subsection Frequencies (CIC Spoken wl)
    '''
    def __init__(self):
        self.words = []
        self.word_freq = dict()
        self.word_rank = dict()

        fh = open('freqlists/spoken.list', 'r')
        rank = 0
        while True:
            line = fh.readline()
            if len(line) == 0:
                break
            row = line.split()
            word = row[0].lower()
            self.words.append(word)
            self.word_freq[word] = float(row[1])
            self.word_rank[word] = rank
            rank += 1


class StatMixedFreqList(FreqList):
    '''
    Statyczna lista frekwencyjna tworzona z kilku innych list frekwencyjnych.\n
    \n
    Uwaga: Tworzenie jej może trwać długo.\n
    Uwaga: Może mieć sumę częstości słów > 1.
    '''
    def __init__(self, flist_weights):
        '''
        Tworzy listę frekwencyjną z kilku innych list.

        :param flist_weights: lista par (lista frekwencyjna, waga); suma wag to 1
        :return: obiekt typu StatMixedFreqList
        '''
        self.words = []
        self.word_freq = dict()
        self.word_rank = dict()

        allwords = sum([flist.words for flist, _ in flist_weights], [])

        for word in allwords:
            s = 0.0
            newf = 0.0
            for (flist, w) in flist_weights:
                f = flist.freq(word)
                if f is not None:
                    s += w
                    newf += w * f
            self.word_freq[word] = newf / s

        freq_word = [(f, w) for (w, f) in self.word_freq.items()]

        freq_word.sort(reverse=True)

        for (_, word) in freq_word:
            self.word_rank[word] = len(self.words)
            self.words.append(word)


class DynMixedFreqList(FreqList):
    '''
    Dynamiczna lista frekwencyjna tworzona z kilku innych list frekwencyjnych.\n
    Częstotliwości słów są wyliczanie na bieżąco.\n
    \n
    Uwaga: Nie ma metod rank, word, dump.\n
    Uwaga: Tworzenie jej trwa krótko.\n
    Uwaga: Może mieć sumę częstości słów > 1.
    '''
    def __init__(self, flist_weights):
        '''
        Tworzy listę frekwencyjną z kilku innych list.

        :param flist_weights: lista par (lista frekwencyjna, waga); suma wag to 1
        :return: obiekt typu DynMixedFreqList
        '''
        self.words = None
        self.word_freq = None
        self.word_rank = None

        self.rank = None
        self.word = None
        self.dump = None

        self.flist_weights = flist_weights

    def freq(self, word):
        '''
        Zwraca częstość słowa.

        :param word: słowo angielskie
        :return: częstość słowa
        '''
        s = 0.0
        newf = 0.0
        for (flist, w) in self.flist_weights:
            f = flist.freq(word)
            if f is not None:
                s += w
                newf += w * f
        return newf / s


FREQLIST = FreqList(filename='freqlist.p')

if __name__ == '__main__':
    print(FREQLIST.rank('cry'))
    print(FREQLIST.rank('cried'))

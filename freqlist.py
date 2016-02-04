import pickle


class FreqList:
    def __init__(self, filename=None, stream=None):
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
        return self.word_freq.get(word, None)

    def rank(self, word):
        return self.word_rank.get(word, None)

    def word(self, rank):
        if rank >= len(self.words):
            return None
        return self.words[rank]

    def dump(self, filename):
        pickle.dump((self.words, self.word_freq, self.word_rank), open(filename, 'wb'))


class PGFreqList(FreqList):  # freqlists/pg.info
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


class OSFreqList(FreqList):  # freqlists/opensubtitles.info
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


class NGSLFreqList(FreqList):  # freqlists/ngsl.info
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


class SpokenFreqList(FreqList):  # freqlists/spoken.info
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


class StatMixedFreqList(FreqList):  # może mieć sumę częstości > 1
    def __init__(self, flist_weights):
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


class DynMixedFreqList(FreqList):  # może mieć sumę częstości > 1
    def __init__(self, flist_weights):
        self.words = None
        self.word_freq = None
        self.word_rank = None

        self.rank = None
        self.word = None
        self.dump = None

        self.flist_weights = flist_weights

    def freq(self, word):
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

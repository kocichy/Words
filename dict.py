import re
import time
import threading


FILENAME = 'dicts/angielsko-polski.txt'


class Dict:
    '''
    Klasa opisująca WIELKI SŁOWNIK ANGIELSKO-POLSKI V.07.2011 (http://www.slowniki.org.pl/eng.html)
    '''
    def __init__(self):
        '''
        Tworzy pusty słownik z pliku.

        :return: obiekty typu Dict
        '''
        self.ready = False

    def load(self):
        '''
        Ładuje nowy słownik z pliku.

        :return: None
        '''
        self.__bad_good = dict()
        self.__ang_pol = dict()

        regex = re.compile('(.+)=(.+)')

        fh = open(FILENAME, 'r', encoding='utf8')
        while True:
            line = fh.readline()
            if len(line) == 0:
                break
            match = regex.match(line)
            if match is not None:
                ang = match.group(1)
                pol = match.group(2)
                low_ang = ang.lower()

                self.__bad_good[low_ang] = ang
                self.__bad_good[ang] = ang

                pols = self.__ang_pol.get(ang, None)
                if pols is None:
                    pols = []
                pols.append(pol)
                self.__ang_pol[ang] = pols
        self.ready = True

    def wait(self):
        '''
        Czeka dopóki słownik nie jest gotowy.

        :return: None
        '''
        while not self.ready:
            pass

    def correct(self, word):
        '''
        Poprawia ang. słowo (np. z "tom" na "Tom").

        :param word: ang. słowo
        :return: poprawione ang. słowo
        '''
        self.wait()
        return self.__bad_good.get(word.lower(), None)

    def pol(self, ang):
        '''
        Zwraca polskie tłumaczenie angielskiego słowa.

        :param ang: ang. słowo
        :return: pol. słowo
        '''
        self.wait()
        cor = self.correct(ang)
        if cor is None:
            return None
        return self.__ang_pol.get(cor, None)

    def exists(self, ang):
        '''
        Sprawdza, czy słowo istnieje w słowniku.

        :param ang: ang. słowo
        :return: czy słowo istnieje w słowniku
        '''
        self.wait()
        return self.correct(ang) is not None


DICT = Dict()


def threaded_load():
    # print("Loading the dictionary...")
    start = time.time()
    DICT.load()
    end = time.time()
    # print("The dictionary has been loaded in %f s" % (end - start))

thread = threading.Thread(target=threaded_load)
thread.start()





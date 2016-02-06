import re


FILENAME = 'dicts/angielsko-polski.txt'


class Dict:
    '''
    Klasa opisująca WIELKI SŁOWNIK ANGIELSKO-POLSKI V.07.2011 (http://www.slowniki.org.pl/eng.html)
    '''
    def __init__(self):
        '''
        Tworzy słownik z pliku.

        :return: obiekty typu Dict
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

    def correct(self, word):
        '''
        Poprawia ang. słowo (np. z "tom" na "Tom").

        :param word: ang. słowo
        :return: poprawione ang. słowo
        '''
        return self.__bad_good.get(word.lower(), None)

    def pol(self, ang):
        '''
        Zwraca polskie tłumaczenie angielskiego słowa.

        :param ang: ang. słowo
        :return: pol. słowo
        '''
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
        return self.correct(ang) is not None

DICT = Dict()

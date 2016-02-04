import re


FILENAME = 'dicts/angielsko-polski.txt'


class Dict:
    def __init__(self, new=False):
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
        return self.__bad_good.get(word.lower(), None)

    def pol(self, ang):
        cor = self.correct(ang)
        if cor is None:
            return None
        return self.__ang_pol.get(cor, None)

    def exists(self, ang):
        return self.correct(ang) is not None

DICT = Dict()

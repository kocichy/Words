import re
import io


def tokens(stream):
    '''
    Zwraca słowa (spójne ciągi liter) w strumieniu.

    :param stream: strumień znakowy
    :return: słowa (spójne ciągi liter) w strumieniu (generator)
    '''
    word = ''
    while True:
        c = stream.read(1)
        if c == '':
            if word != '':
                yield word
            raise StopIteration
        if c.isalpha():
            word += c
        elif word != '':
            yield word
            word = ''


def normalize(w):
    '''
    Złożenie choose_stem(possible_stems(s.lower()))\n
    Dla argumentu:\n
    1. Zamienia wielkie na małe litery.\n
    2. Tworzy listę potencjalnych tematów.\n
    3. Wybiera najczęstszy temat patrząc na listę frekwencyjną.

    :param s: słowo
    :return: temat słowa
    '''
    return choose_stem(possible_stems(w.lower()))


class Rule:
    '''
    Klasa opisująca zasadę gramatyczną używaną do odgadnięcia tematu słowa.\n
    Np. "moved" -> "move".
    '''
    def __init__(self, pattern, suffix):
        '''
        Konstruktor

        :param pattern: wzorzec jako wyrażenie regularne
        :param suffix: doklejany sufiks do przypasowanej we wzorcu grupy
        :return:
        '''
        self.regex = re.compile(pattern)
        self.suffix = suffix

    def get_stem(self, word):
        '''
        Stusuje na słowie regułę i zwraca możliwy temat.

        :param word: ang. słowo
        :return: temat lub None, jeśli reguła nie pasuje do słowa
        '''
        match = self.regex.match(word)
        if match is None:
            return None
        return match.group(1) + self.suffix


class RuleXXing():
    '''
    Reguła "getting -> get"
    '''
    def __init__(self):
        self.regex = re.compile('(.*)(..)ing$')

    def get_stem(self, word):
        '''
        Stusuje na słowie regułę i zwraca możliwy temat.

        :param word: ang. słowo
        :return: temat lub None, jeśli reguła nie pasuje do słowa
        '''
        match = self.regex.match(word)
        if match is None:
            return None
        xx = match.group(2)
        if xx[0] != xx[1]:
            return None
        return match.group(1) + match.group(2)[0]


class RuleXXed():
    '''
    Reguła "stopped -> stop"
    '''
    def __init__(self):
        self.regex = re.compile('(.*)(..)ed$')

    def get_stem(self, word):
        '''
        Stusuje na słowie regułę i zwraca możliwy temat.

        :param word: ang. słowo
        :return: temat lub None, jeśli reguła nie pasuje do słowa
        '''
        match = self.regex.match(word)
        if match is None:
            return None
        xx = match.group(2)
        if xx[0] != xx[1]:
            return None
        return match.group(1) + match.group(2)[0]


RULES = [Rule('(.*)ed$', 'e'),      # moved     -> move
         Rule('(.*)ed$', ''),       # asked     -> ask
         Rule('(.*)ied$', 'y'),     # cried     -> cry

         Rule('(.*)ing$', ''),      # playing   -> play
         RuleXXing(),               # getting   -> get
         RuleXXed(),                # stopped   -> stop

         Rule('(.*)es$', ''),       # misses    -> miss
         Rule('(.*)s$', '')]        # gives     -> give


def possible_stems(w):
    '''
    Próbuje stosować reguły gramatyczne do argumentu i tworzy listę potencjalnych tematów.

    :param w: ang. słowo
    :return: lista możliwych tematów słowa
    '''
    stems = [w]
    for rule in RULES:
        stem = rule.get_stem(w)
        if stem is not None:
            stems.append(stem)
    return stems


from freqlist import FREQLIST


def choose_stem(stems):
    '''
    Dla listy potencjalnych tematów wybiera najbardziej prawdopodobny temat (najczęstszy).

    :param stems: lista potencjalncych tematów
    :return: najczęściej spotykany w języku temat
    '''
    best_stem = None
    best_f = 0.0
    for stem in stems:
        f = FREQLIST.freq(stem)
        if f is not None and f > best_f:
            best_f = f
            best_stem = stem
    return best_stem


def parse(stream):
    '''
    Dla danego strumienia znakowego zwraca listę tematów występujących w nim słów.

    :param stream: strumień znakowy
    :return: lista tematów
    '''
    words = []
    for token in tokens(stream):
        word = normalize(token)
        if word is not None:
            words.append(word)
    return list(set(words))

if __name__ == '__main__':
    print([w for w in parse(io.StringIO('werq She often sdfsdfa speaks rqwrqw about Mary\'s fiancé.dasdasdas'))])

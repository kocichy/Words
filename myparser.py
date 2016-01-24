import re
import io

def tokens(stream):
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


def normalize(s):
    return choose_stem(possible_stems(s.lower()))


class Rule:
    def __init__(self, pattern, suffix):
        self.regex = re.compile(pattern)
        self.suffix = suffix

    def get_stem(self, word):
        match = self.regex.match(word)
        if match is None:
            return None
        return match.group(1) + self.suffix


class RuleXXing:
    def __init__(self):
        self.regex = re.compile('(.*)(..)ing$')

    def get_stem(self, word):
        match = self.regex.match(word)
        if match is None:
            return None
        xx = match.group(2)
        if xx[0] != xx[1]:
            return None
        return match.group(1) + match.group(2)[0]


class RuleXXed:
    def __init__(self):
        self.regex = re.compile('(.*)(..)ed$')

    def get_stem(self, word):
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


def possible_stems(s):
    stems = [s]
    for rule in RULES:
        stem = rule.get_stem(s)
        if stem is not None:
            stems.append(stem)
    return stems


from freqlist import FREQLIST


def choose_stem(stems):
    best_stem = None
    best_f = 0.0
    for stem in stems:
        f = FREQLIST.freq(stem)
        if f is not None and f > best_f:
            best_f = f
            best_stem = stem
    return best_stem


def parse(stream):
    for token in tokens(stream):
        word = normalize(token)
        if word is not None:
            yield word

if __name__ == '__main__':
    print([w for w in parse(io.StringIO('werq She often sdfsdfa speaks rqwrqw about Mary\'s fiancé.dasdasdas'))])

import unittest
import io
import myparser

class TokensTest(unittest.TestCase):
    inouts = [('_a__bb__cc__ddd__', ['a', 'bb', 'cc', 'ddd']),
              ('aaa___bbb', ['aaa', 'bbb']),
              ('Pójdźże, kiń tę chmurność w głąb flaszy!',
               ['Pójdźże', 'kiń', 'tę', 'chmurność', 'w', 'głąb', 'flaszy'])]

    def test(self):
        for (in_, out_) in self.inouts:
            stream = io.StringIO(in_)
            res = [s for s in myparser.tokens(stream)]
            self.assertEqual(out_, res)


class NormalizeTest(unittest.TestCase):
    inouts = [('Getting', 'get'),
              ('LEAVES', 'leave'),
              ('mOvEd', 'move'),
              ('fIAncé', 'fiancé'),
              ('SPeaks', 'speak'),
              ('DROPPED', 'drop')]

    def test(self):
        for (in_, out_) in self.inouts:
            res = myparser.normalize(in_)
            self.assertEqual(out_, res)


class PossibleStemsTest(unittest.TestCase):
    inouts = [('moved', ['mov', 'move', 'moved']),
              ('asked', ['ask', 'aske', 'asked']),
              ('cried', ['cri', 'crie', 'cried', 'cry']),

              ('playing', ['play', 'playing']),
              ('getting', ['get', 'gett', 'getting']),
              ('stopped', ['stop', 'stopp', 'stoppe', 'stopped']),

              ('misses', ['miss', 'misse', 'misses']),
              ('gives', ['giv', 'give', 'gives'])]

    def test(self):
        for (in_, out_) in self.inouts:
            res = myparser.possible_stems(in_)
            res.sort();
            out_.sort();
            self.assertEqual(res, out_)


class ChooseStemTest(unittest.TestCase):
    inouts = [(['mov', 'move', 'moved'], 'move'),
              (['ask', 'aske', 'asked'], 'ask'),
              (['cri', 'crie', 'cried', 'cry'], 'cried'),  # dziwne

              (['play', 'playing'], 'play'),
              (['get', 'gett', 'getting'], 'get'),
              (['stop', 'stopp', 'stoppe', 'stopped'], 'stop'),

              (['miss', 'misse', 'misses'], 'miss'),
              (['giv', 'give', 'gives'], 'give')]

    def test(self):
        for (in_, out_) in self.inouts:
            res = myparser.choose_stem(in_)
            self.assertEqual(res, out_)

if __name__ == '__main__':
    unittest.main()

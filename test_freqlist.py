import unittest
import freqlist
import io


class PGFreqListTest(unittest.TestCase):
    def test_operations(self):
        fl = freqlist.PGFreqList()

        self.assertEqual(fl.word(0), 'the')
        self.assertEqual(fl.word(36661), 'zoetrope')
        self.assertEqual(fl.word(36662), None)

        self.assertEqual(fl.freq('mary'), 0.000108633)
        self.assertEqual(fl.freq('france'), 0.000151108)
        self.assertEqual(fl.freq('aaabbbccc'), None)

        self.assertEqual(fl.rank('aaaaaaaa'), None)
        self.assertEqual(fl.rank('a'), 84)
        self.assertEqual(fl.rank('calves'), 9998)


class OSFreqListTest(unittest.TestCase):
    def test_operations(self):
        fl = freqlist.OSFreqList()

        self.assertEqual(fl.word(0), 'you')
        self.assertEqual(fl.word(456630), 'theydropped')
        self.assertEqual(fl.word(456631), None)

        self.assertEqual(fl.freq('you'), 0.043205204411557445)
        self.assertEqual(fl.freq('sorry'), 0.0011253366622264351)
        self.assertEqual(fl.freq('quechulo'), 6.87871209268162e-09)

        self.assertEqual(fl.rank('aaaaaaaa'), None)
        self.assertEqual(fl.rank('a'), 4)
        self.assertEqual(fl.rank('calves'), 14473)


class NGSLFreqListTest(unittest.TestCase):
    def test_operations(self):
        fl = freqlist.NGSLFreqList()

        self.assertEqual(fl.word(0), 'the')
        self.assertEqual(fl.word(31240), 'victimizer')
        self.assertEqual(fl.word(31241), None)

        self.assertEqual(fl.freq('of'), 0.0310978476671406)
        self.assertEqual(fl.freq('username'), 3.17966727479204e-07)
        self.assertEqual(fl.freq('relict'), 4.3857479652304e-08)

        self.assertEqual(fl.rank('aaaaaaaa'), None)
        self.assertEqual(fl.rank('a'), 5)
        self.assertEqual(fl.rank('calve'), 14549)


class SpokenFreqListTest(unittest.TestCase):
    def test_operations(self):
        fl = freqlist.SpokenFreqList()

        self.assertEqual(fl.word(0), 'be')
        self.assertEqual(fl.word(24036), 'aaagh')
        self.assertEqual(fl.word(24037), None)

        self.assertEqual(fl.freq('of'), 0.018917797388677)
        self.assertEqual(fl.freq('username'), None)
        self.assertEqual(fl.freq('adv'), 1.78988176971768e-07)

        self.assertEqual(fl.rank('aaaaaaaa'), None)
        self.assertEqual(fl.rank('a'), 6)
        self.assertEqual(fl.rank('calve'), 23832)


class FreqListTest(unittest.TestCase):
    def test_init_from_stream(self):
        fl = freqlist.FreqList(stream=io.StringIO(' a.A.a-i-I-b'))

        self.assertEqual(fl.word(0), 'a')
        self.assertEqual(fl.word(2), 'b')
        self.assertEqual(fl.word(3), None)

        self.assertEqual(fl.freq('a'), 1/2)
        self.assertEqual(fl.freq('i'), 1/3)
        self.assertEqual(fl.freq('c'), None)

        self.assertEqual(fl.rank('x'), None)
        self.assertEqual(fl.rank('a'), 0)
        self.assertEqual(fl.rank('b'), 2)


if __name__ == '__main__':
    unittest.main()

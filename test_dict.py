import unittest
from dict import DICT


class DictTest(unittest.TestCase):
    def test_DICT(self):
        self.assertEqual(DICT.pol('abases'), ['martwić'])
        self.assertEqual(DICT.pol('abbey'), ['opactwo'])
        self.assertEqual(DICT.pol('zymosis'), ['fermentacja'])
        self.assertEqual(DICT.pol("Abel's integral equation"), ['równanie całkowe Abela'])
        self.assertEqual(DICT.correct("abel's integral equation"), "Abel's integral equation")
        self.assertEqual(DICT.correct("laplacian"), "Laplacian")
        self.assertEqual(DICT.correct("LaplAcIAN"), "Laplacian")
        self.assertEqual(DICT.correct("LaPLacIan"), "Laplacian")


if __name__ == '__main__':
    unittest.main()

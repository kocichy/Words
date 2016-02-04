import unittest
import freqlist
import selector
import io
import database
import os


class SelectorTest(unittest.TestCase):
    dbfilename = 'test_selector.db'

    def setUp(self):
        str_ = 'a a a a a a | b b b b b | c c c c | d d d | e e | f'
        self.fl = freqlist.FreqList(stream=io.StringIO(str_))

        try:
            os.remove(self.dbfilename)
        except:
            pass

        self.db = database.Database(self.dbfilename, new=True)
        self.db.modify_word('a', self.fl.rank('a'), True, True)
        self.db.modify_word('b', self.fl.rank('b'), True, False)
        self.db.modify_word('c', self.fl.rank('c'), False, True)
        self.db.modify_word('d', self.fl.rank('d'), True, True)

    def tearDown(self):
        self.db.con.close()
        os.remove(self.dbfilename)

    def test_get_pr_func(self):
        pr = selector.get_pr_func(db=self.db, fl=self.fl, max_=6, step=2)
        self.assertEqual(pr('a'), 1.0)
        self.assertEqual(pr('b'), 1.0)
        self.assertEqual(pr('c'), 0.75)
        self.assertEqual(pr('d'), 0.5)
        self.assertEqual(pr('e'), 0.4)
        self.assertEqual(pr('f'), 0.3)
        self.assertEqual(pr('g'), 0.01)

if __name__ == '__main__':
    unittest.main()

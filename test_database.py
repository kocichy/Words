import unittest
import sqlite3
import os
import time
from database import Database


class DataaseCase(unittest.TestCase):
    filename = 'test_datebase.db'

    def setUp(self):
        try:
            os.remove(self.filename)
        except:
            pass
        db = Database(self.filename, new=True)

    def tearDown(self):
        os.remove(self.filename)

    def test_create(self):
        con = sqlite3.connect(self.filename)
        cur = con.execute("SELECT * from Word;")
        col_names = [description[0] for description in cur.description]
        self.assertEqual(col_names, ['word', 'rank', 'known_earlier', 'known_now', 'mod_time'])

        rows = cur.fetchall()
        self.assertEqual(rows, [])

    def test_modify_word(self):
        con = sqlite3.connect(self.filename)

        cur = con.execute("SELECT * from Word;")
        rows = cur.fetchall()
        self.assertEqual(rows, [])

        db = Database(self.filename)
        db.modify_word('x', 0, True, False)
        cur = con.execute("SELECT * from Word;")
        rows = [(a, b, c, d) for (a, b, c, d, _) in cur.fetchall()]
        self.assertEqual(rows, [('x', 0, True, False)])

        cur = con.execute("SELECT mod_time from Word WHERE word = 'x';")
        mod_time1 = cur.fetchall()[0][0]

        time.sleep(1)

        db.modify_word('x', 1, True, True)
        cur = con.execute("SELECT * from Word;")
        rows = [(a, b, c, d) for (a, b, c, d, _) in cur.fetchall()]
        self.assertEqual(rows, [('x', 1, True, True)])

        cur = con.execute("SELECT mod_time from Word WHERE word = 'x';")
        mod_time2 = cur.fetchall()[0][0]

        self.assertNotEqual(mod_time1, mod_time2)

    def test_known_earlier(self):
        db = Database(self.filename)
        db.modify_word('a', 0, known_earlier=True, known_now=False)
        db.modify_word('b', 0, known_earlier=False, known_now=False)
        self.assertEqual(db.known_earlier('a'), True)
        self.assertEqual(db.known_earlier('b'), False)
        self.assertEqual(db.known_earlier('c'), False)

    def test_known_now(self):
        db = Database(self.filename)
        db.modify_word('k', 0, known_earlier=True, known_now=False)
        db.modify_word('l', 0, known_earlier=False, known_now=True)
        self.assertEqual(db.known_now('k'), False)
        self.assertEqual(db.known_now('l'), True)
        self.assertEqual(db.known_now('m'), False)

    def test_known_words(self):
        db = Database(self.filename)
        db.modify_word('q', 1000, known_earlier=True, known_now=False)
        db.modify_word('w', 1001, known_earlier=False, known_now=True)
        db.modify_word('e', 1002, known_earlier=True, known_now=False)
        db.modify_word('r', 1003, known_earlier=False, known_now=True)
        db.modify_word('t', 1004, known_earlier=False, known_now=True)
        self.assertEqual(db.known_words(1000, 1000), None)
        self.assertEqual(db.known_words(1005, 1009), None)
        self.assertEqual(db.known_words(1000, 1001), 1/1)
        self.assertEqual(db.known_words(1000, 1002), 1/2)
        self.assertEqual(db.known_words(1000, 1005), 2/5)

if __name__ == '__main__':
    unittest.main()

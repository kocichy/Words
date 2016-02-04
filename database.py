import sqlite3


class Database:

    @staticmethod
    def read_com(filename):
        file = open(filename, 'r')
        return file.read()

    create_com = read_com.__func__('sql/create.sql')
    known_words_com = read_com.__func__('sql/known_words.sql')
    modify_com = "INSERT OR REPLACE INTO Word(word, rank, known_earlier, known_now) VALUES (?, ?, ?, ?);"
    known_ealier_com = "SELECT * FROM Word WHERE word = ? AND known_earlier = 1;"
    known_now_com = "SELECT * FROM Word WHERE word = ? AND known_now = 1;"
    exists_com = "SELECT * FROM Word WHERE word = ?;"
    clear_com = 'DROP TABLE IF EXISTS Word;'

    def __init__(self, filnename, new=False):
        self.filename = filnename
        self.con = sqlite3.connect(self.filename)
        if new:
            self.con.execute(Database.create_com)

    def modify_word(self, word, rank, known_earlier, known_now):
        cur = self.con.cursor()
        cur.execute(self.modify_com, (word, rank, known_earlier, known_now))
        self.con.commit()

    def known_earlier(self, word):
        cur = self.con.cursor()
        cur.execute(self.known_ealier_com, (word,))
        rows = cur.fetchall()
        return len(rows) > 0

    def known_now(self, word):
        cur = self.con.cursor()
        cur.execute(self.known_now_com, (word,))
        rows = cur.fetchall()
        return len(rows) > 0

    def known_words(self, a, b):
        cur = self.con.cursor()
        cur.execute(self.known_words_com, (a, b, a, b))
        res = cur.fetchall()
        return res[0][0]

    def exists(self, word):
        cur = self.con.cursor()
        cur.execute(self.exists_com, (word,))
        rows = cur.fetchall()
        return len(rows) > 0

    def clear(self):
        self.con.execute(Database.clear_com)
        self.con.execute(Database.create_com)

DATABASE = Database('database.db')

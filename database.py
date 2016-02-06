import sqlite3


class Database:
    '''
    Klasa obsługująca bazę danych, w której znajdują się informacje o słownictwie użytkownika.
    '''
    @staticmethod
    def __read_com(filename):
        file = open(filename, 'r')
        return file.read()

    __create_com = __read_com.__func__('sql/create.sql')
    __known_words_com = __read_com.__func__('sql/known_words.sql')
    __modify_com = "INSERT OR REPLACE INTO Word(word, rank, known_earlier, known_now) VALUES (?, ?, ?, ?);"
    __known_ealier_com = "SELECT * FROM Word WHERE word = ? AND known_earlier = 1;"
    __known_now_com = "SELECT * FROM Word WHERE word = ? AND known_now = 1;"
    __exists_com = "SELECT * FROM Word WHERE word = ?;"
    __clear_com = 'DROP TABLE IF EXISTS Word;'

    def __init__(self, filnename, new=False):
        '''
        Konstruktor

        :param filnename: nazwa pliku *.db
        :param new: czy utworzyć nową bazę (True/False)
        :return: obiekt typu Database
        '''
        self.filename = filnename
        self.con = sqlite3.connect(self.filename)
        if new:
            self.clear()

    def modify_word(self, word, rank, known_earlier, known_now):
        '''
        Modyfikuje lub dodaje informacje o słowie w bazie danych.

        :param word: słowo
        :param rank: pozycja na liście frekwencyjnej
        :param known_earlier: czy słowo było znane w momencie dodawania do bazy
        :param known_now: czy słowo zostanie przyswojone
        :return:
        '''
        cur = self.con.cursor()
        cur.execute(self.__modify_com, (word, rank, known_earlier, known_now))
        self.con.commit()

    def known_earlier(self, word):
        '''
        Zwraca, czy słowo było znane w momencie dodania do bazy.

        :param word: ang. słowo
        :return: czy słowo było znane w momencie dodania do bazy
        '''
        cur = self.con.cursor()
        cur.execute(self.__known_ealier_com, (word,))
        rows = cur.fetchall()
        return len(rows) > 0

    def known_now(self, word):
        '''
        Zwraca, czy słowo jest znane lub będzie znane.

        :param word: ang. słowo
        :return: czy słowo jest znane lub będzie znane
        '''
        cur = self.con.cursor()
        cur.execute(self.__known_now_com, (word,))
        rows = cur.fetchall()
        return len(rows) > 0

    def known_words(self, a, b):
        '''
        Zwraca część znanych słów na przedziale [a, b) na liście frekwencyjnej

        :param a: mniejsza pozycja na liście frekwencyjnej
        :param b: większa pozycja na liście frekwencyjnej
        :return: część znanych słów na przedziale [a, b) na liście frekwencyjnej
        '''
        cur = self.con.cursor()
        cur.execute(self.__known_words_com, (a, b, a, b))
        res = cur.fetchall()
        return res[0][0]

    def exists(self, word):
        '''
        Zwraca, czy dane słowo istnieje w bazie danych.

        :param word: ang. słowo
        :return: czy dane słowo istnieje w bazie danych
        '''
        cur = self.con.cursor()
        cur.execute(self.__exists_com, (word,))
        rows = cur.fetchall()
        return len(rows) > 0

    def clear(self):
        '''
        Usuwa dane w bazie danych

        :return: None
        '''
        self.con.execute(Database.__clear_com)
        self.con.execute(Database.__create_com)

DATABASE = Database('database.db')

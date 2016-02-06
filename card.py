from dict import DICT
import sqlite3
import os
import zipfile
from contextlib import suppress
import uuid
import time
import random
from shutil import copyfile


class Card:
    '''
    Klasa opisuje fiszkę.
    '''
    def __init__(self, word):
        '''
        Konstruktor

        :param word: angielskie słowo
        :return: fiszka
        '''
        self.ang = DICT.correct(word)
        self.pol = Card.__pol_str(self.ang)

    @staticmethod
    def __pol_str(ang):
        pols = DICT.pol(DICT.correct(ang))
        res = ""
        for i in range(0, len(pols)):
            pol = pols[i]
            if i != len(pols)-1:
                res += pol + ", "
            else:
                res += pol
        return res


def write_apkg(words, filename):
    '''
    Tworzy zbiór fiszek ze słów i zapisuje je do pliku w formacie APKG.

    :param words: lista angielskich słów
    :param filename: nazwa pliku do zapisu
    :return: None
    '''
    cards = [Card(word) for word in words]
    __cards_to_sql(cards, "temp/temp.sql")
    __sql_to_apkg('temp/temp.sql', 'temp/temp.apkg')
    copyfile('temp/temp.apkg', filename)


def __cards_to_sql(cards, sqlfname):
    schemafh = open('sql/schema.sql', 'r')
    sql = schemafh.read()
    sqlfh = open(sqlfname, 'w')
    sqlfh.write(sql)

    for card in cards:
        ins_note = "INSERT INTO notes VALUES (%d,'%s',1342701190172,%d,-1,'','%s','%s',1467122191,0,'');\n"
        tup = (random.randrange(1000*1000*1000), uuid.uuid4(), time.time(), card.pol + str(chr(31)) + card.ang, card.pol)
        ins_note = ins_note % tup

        note_id = tup[0]
        mod = tup[2]

        ins_card = "INSERT INTO cards VALUES (%d,%d,1342701190228,0,%d,-1,0,0,177,0,2500,0,0,0,0,0,0,'');\n"
        tup = (random.randrange(1000*1000*1000), note_id, mod)
        ins_card = ins_card % tup

        sqlfh.write(ins_note)
        sqlfh.write(ins_card)

    sqlfh.write("COMMIT;\n")
    sqlfh.close()


def __sql_to_apkg(sqlfname, apkgfname):
    with suppress(Exception):
        os.remove('temp/collection.anki2')

    sqlfh = open(sqlfname, 'r')
    sql = sqlfh.read()

    con = sqlite3.connect('temp/collection.anki2')
    con.executescript(sql)

    mediafh = open('temp/media', 'w')
    mediafh.write('{}')
    mediafh.close()

    zipfh = zipfile.ZipFile(apkgfname, 'w')
    zipfh.write(filename='temp/collection.anki2', arcname='collection.anki2')
    zipfh.write(filename='temp/media', arcname='media')

if __name__ == '__main__':
    write_apkg(['cry', 'lead'], 'temp/gotowy.apkg')

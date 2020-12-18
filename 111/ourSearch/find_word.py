#!/bin/python3
import sqlite3

def find_word(word):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    #word = ("занятий",)

    #получаем список url и их id из бд
    sql = "SELECT * FROM ourSearch_urltable"
    cursor.execute(sql)
    urls = cursor.fetchall()

    #получаем id слова из бд слов
    sql = ("SELECT idword FROM ourSearch_wordstable WHERE word=?")
    cursor.execute(sql, (word,))
    ID = cursor.fetchall()
    if len(ID) == 0:                    #если такого слова вообще нет в бд, то выходим
        print("No such word in db")
        conn.close()
        exit()
#print(ID[0][0])

#идем по ссылкам и ищем там слово
    for i in range(len(urls)):

        sql = "SELECT count FROM ourSearch_counttable WHERE idword_id = ? AND idurl_id = ?"
        filter = (ID[0][0], urls[i][1])
        cursor.execute(sql,filter)
        count = cursor.fetchall()
        if (len(count)) > 0:
            print(count[0][0])
            return(urls[i][0])
        else:
            print("No such word in this url")

    conn.close()

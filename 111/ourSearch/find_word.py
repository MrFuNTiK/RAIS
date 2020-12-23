#!/usr/bin/python3
import pymysql

def find_word(word):

    rez_urls = []
    conn = pymysql.connect("212.192.123.98", "736_4", "L%jE6gQ1bx", "736_4")
    cursor = conn.cursor()


    #получаем id слова из бд слов
    sql = ("SELECT idword FROM ourSearch_wordstable WHERE word=%s")
    cursor.execute(sql, (word,))
    ID = cursor.fetchall()
    if len(ID) == 0:                    #если такого слова вообще нет в бд, то выходим
        #print("No such word in db")
        conn.close()
        return rez_urls
    #print(ID[0][0])

    #идем по ссылкам и ищем там слово


    sql = "SELECT count, idurl_id FROM ourSearch_counttable WHERE idword_id = %s ORDER BY count DESC"
    filter = (ID[0][0],)
    cursor.execute(sql,filter)
    count = cursor.fetchall()
    if len(count) > 0:
        for i in range(len(count)):
            sql = "SELECT urladress FROM ourSearch_urltable WHERE idurl=%s"
            cursor.execute(sql, (count[i][1],))
            url = cursor.fetchall()
            rez_urls.append(url[0][0])
    #print(count[0][1])
    #print(rez_urls)

    conn.close()
    return rez_urls

word = "строка"
rez = find_word(word)
print(rez)
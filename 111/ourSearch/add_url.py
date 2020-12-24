#!/usr/bin/python3
import pymysql
import requests

def add_url(url):
    req = requests.get(url)
    if req.status_code == 200:      #если ссылка рабочая, то добавляем в бд

        #ДОБАВЛЕНИЕ ЧЕРЕЗ SQLITE3
        #cursor = connection.cursor()
        conn = pymysql.connect("212.192.123.98", "736_4", "L%jE6gQ1bx", "736_4")
        cursor = conn.cursor()

        dataToAdd = (url,)

        sql = "INSERT INTO ourSearch_urltable(urladress) VALUES(%s)"
        cursor.execute(sql, dataToAdd)
        conn.commit()
        conn.close()


        
        print("New url successfully added")
    else:                           #иначе ошибка
        print("Bad url")


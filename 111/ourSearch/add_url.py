#!/bin/python3
import sqlite3
import requests


"""
def get_page(url):
    req = requests.get(url)

    if req.status_code == 200:
    return None
"""
def add_url(url):
#url = "https://timetable.tusur.ru/faculties/fb/groups/736-6"
    req = requests.get(url)
    if req.status_code == 200:      #если ссылка рабочая, то добавляем в бд
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()

        dataToAdd = (url,)

        sql = "INSERT INTO ourSearch_urltable(urladress) VALUES(?)"
        cursor.execute(sql, dataToAdd)
        conn.commit()
        conn.close()
        print("New url successfully added")
    else:                           #иначе ошибка
        print("Bad url")

#!/usr/bin/python3
import sqlite3
import requests


def rm_url(url):
    def get_page(url):
        req = requests.get(url)

        if req.status_code == 200:
            return None


    dataToSearch = (url,)



    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    sql = "SELECT idurl FROM ourSearch_urltable WHERE urladress=%s"
    cursor.execute(sql, dataToSearch)
    ID = cursor.fetchall()
    if len(ID) != 0:
        urlToRemove = (ID[0][0],)
        sql = "DELETE FROM ourSearch_urltable WHERE idurl=%s"
        cursor.execute(sql, urlToRemove)
        conn.commit()
        conn.close()
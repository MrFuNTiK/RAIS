#!/usr/bin/python3
import pymysql
#import requests


"""
def get_page(url):
    req = requests.get(url)

    if req.status_code == 200:
    return None
"""
url = "https://timetable.tusur.ru/faculties/fb/groups/736-1"
dataToSearch = (url,)



conn = pymysql.connect("212.192.123.98", "736_4", "L%jE6gQ1bx", "736_4")
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
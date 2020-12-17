#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()


sql = "SELECT * FROM ourSearch_counttable"
cursor.execute(sql)
print(cursor.fetchall())



sql = "SELECT * FROM ourSearch_wordstable"
cursor.execute(sql)
print(cursor.fetchall())


#"""
sql = "SELECT * FROM ourSearch_urltable"
cursor.execute(sql)
print(cursor.fetchall())
#"""

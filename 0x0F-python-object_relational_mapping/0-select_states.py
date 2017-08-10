#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa
import MySQLdb
db = MySQLdb.connect(user="root", db="hbtn_0e_0_usa")
cursor = db.cursor()
cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
data = cursor.fetchone()
while data is not None:
    print(data)
    data = cursor.fetchone()
db.close()

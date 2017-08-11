#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, name FROM states WHERE name like 'N%' ORDER BY id ASC")
    data = cursor.fetchone()
    while data is not None:
        print(data)
        data = cursor.fetchone()
    cursor.close()
    db.close()

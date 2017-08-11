#!/usr/bin/python3
# lists all cities from the database hbtn_0e_4_usa
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
        INNER JOIN states ON state_id=states.id ORDER BY cities.id ASC")
    data = cursor.fetchone()
    while data is not None:
        print(data)
        data = cursor.fetchone()
    cursor.close()
    db.close()

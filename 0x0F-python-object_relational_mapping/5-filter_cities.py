#!/usr/bin/python3
# takes in the name of a state as an argument and lists all cities of that state
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name \
        FROM cities \
        INNER JOIN states \
        ON state_id=states.id \
        WHERE states.name='{}' \
        ORDER BY cities.id ASC".format(sys.argv[4]))
    data = cursor.fetchone()
    while data is not None:
        print("".join(map(str, data)), end=", ")
        data = cursor.fetchone()
    cursor.close()
    db.close()

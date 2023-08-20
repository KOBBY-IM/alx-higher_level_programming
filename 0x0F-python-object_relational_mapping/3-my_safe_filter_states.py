#!/usr/bin/python3
"""
Peturn matching states; safe from MySQL injections
Parameters given to script: username, password, database, state to match
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL; match arg given
    cursor = db.cursor()
    cursor.execute("""
    SELECT *
    FROM states
    WHERE name LIKE %s
    ORDER BY id""", (argv[4], ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

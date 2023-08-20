#!/usr/bin/python3
"""
Return info from both tables (tables 'cities' 'states)
Parameters given to script: username, password, database
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

    # create cursor to exec queries using SQL; join two tables for all info
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT id,
        name,
        (SELECT name FROM states WHERE state_id=id)
        FROM cities ORDER BY id
        """
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

#!/usr/bin/python3
"""
Return all table values('states')
Parameters given to script: username, password, database
"""

from sys import argv
import MySQLdb

if __name__ = "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                        port=3306,
                        user=argv[1],
                        password=argv[2],
                        database=argv[3])

    # create user to execute queries
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)


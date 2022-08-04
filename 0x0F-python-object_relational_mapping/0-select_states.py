#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
Arguments:
    mysql username sys.argv[1]
    mysql password sys.argv[2]
    database name sys.argv[3]
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    for row in curs.fetchall():
        print(row)
    curs.close()
    db.close()

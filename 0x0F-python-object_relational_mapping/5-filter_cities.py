#!/usr/bin/env python3
"""
lists all cities from the database hbtn_0e_0_usa
fix injection
Arguments:
    mysql username sys.argv[1]
    mysql password sys.argv[2]
    database name sys.argv[3]
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )
    curs = db.cursor()
    curs.execute(
       "SELECT cities.name\
        FROM cities JOIN states\
        ON cities.state_id = states.id WHERE states.name = %s\
        ORDER BY cities.id\
        ", (argv[4],))
    for row in curs.fetchall():
        print(row)
    curs.close()
    db.close()

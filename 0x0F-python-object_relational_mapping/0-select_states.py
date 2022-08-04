#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':

  db = MySQLdb.connect(
    host='localhost',
    port=3306,
    passwd=sys.argv[2],
    user= sys.argv[1],
    db= sys.argv[3]
    )
  cur = db.cursor("SHOW TABLES")

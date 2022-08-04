#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(
  host='localhost', port='3306', passwd='',user='root', db='hbtn_0e_0_usa')
cur = db.cursor("SHOW TABLES")

#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
      host='localhost',
      port=3306,
      user=argv[1],
      passwd=argv[2],
      db=argv[3],
      charset="utf8"
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

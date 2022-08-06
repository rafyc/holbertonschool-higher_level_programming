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
        """
        SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE states.id = cities.state_id
        ORDER BY id ASC
        """
        )
    for row in curs.fetchall():
        print(row)
    curs.close()
    db.close()

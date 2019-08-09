#!/usr/bin/python3
"""search display hits in a db table matching an arg passed by the user"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
                .format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()

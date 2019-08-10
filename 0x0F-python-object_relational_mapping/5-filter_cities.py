#!/usr/bin/python3
"""list all cities from db table"""

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
    cur.execute("SELECT cities.name\
    FROM cities INNER JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name LIKE %s\
    ORDER BY cities.id ASC",
                (argv[4],))
    query_rows = cur.fetchall()
    lis = []
    for item in query_rows:
        lis.append(item[0])
    print(", ".join(lis))
    cur.close()

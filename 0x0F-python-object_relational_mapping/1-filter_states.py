#!/usr/bin/python3

"""
script that lists all states with a name starting with N (upper N)
 from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_conn = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM states WHERE (name LIKE BINARY 'N%' )\
    ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_conn.close()

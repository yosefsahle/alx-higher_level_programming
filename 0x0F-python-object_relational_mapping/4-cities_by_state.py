#!/usr/bin/python3
"""
python script  that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db_conn = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db_conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_conn.close()

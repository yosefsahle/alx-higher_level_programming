#!/usr/bin/python3
"""
python script  that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db_conn = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    state_name = argv[4]
    cursor = db_conn.cursor()
    cursor.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    AND states.name = '{:s}'\
                    ORDER BY cities.id ASC".format(state_name))
    rows = cursor.fetchall()
    res = []
    for i in rows:
        res.append(i[0])

    print(", ".join(res))

    cursor.close()
    db_conn.close()

#!/usr/bin/env python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
SQL injection safe"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("""SELECT `name` FROM `cities`
                 WHERE `state_id` = (
                 SELECT `id` FROM `states`
                 WHERE `name` = %s);""", (sys.argv[4],))
    cities = curr.fetchall()
    for i in range(len(cities)):
        if i < len(cities) - 1:
            print("{}, ".format(cities[i][0]), end='')
        else:
            print(cities[i][0])
    curr.close()
    db.close()

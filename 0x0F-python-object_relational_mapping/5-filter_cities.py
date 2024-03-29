#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    """List all cities from a state given as argument"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("""SELECT `name` FROM `cities`
                 WHERE `state_id` = (
                 SELECT `id` FROM `states`
                 WHERE `name` LIKE %s)
                 ORDER BY `id` ASC;""", (sys.argv[4],))
    cities = curr.fetchall()
    citiesNames = [city[0] for city in cities]
    print(', '.join(citiesNames))
    curr.close()
    db.close()

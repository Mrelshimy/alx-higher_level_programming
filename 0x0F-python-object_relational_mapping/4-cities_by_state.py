#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    """List all cities including state name"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("""SELECT `cities`.`id`, `cities`.`name`,
                 `states`.`name` FROM `cities`
                 JOIN `states` ON `states`.`id` = `cities`.`state_id`
                 ORDER BY `cities`.`id`;""")
    cities = curr.fetchall()
    for city in cities:
        print(city)
    curr.close()
    db.close()

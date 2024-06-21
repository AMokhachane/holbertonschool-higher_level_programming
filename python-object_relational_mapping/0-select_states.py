import MySQLdb as DB
import sys


db_connect = DB.connect(
    host='localhost',
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3])


if __name__ == '__main__':
    db_cursor = db_connect.cursor()

    db_cursor.execute("CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;")
    db_cursor.execute("USE hbtn_0e_0_usa;")
    db_cursor.execute(
        """CREATE TABLE IF NOT EXISTS states(
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(256) NOT NULL,
            PRIMARY KEY (id)
        )"""
    )

    states = ("California", "Arizona", "Texas", "New york", "Nevada")

    for state in states:
        db_cursor.execute("INSERT INTO states (name) VALUES (%s)", [state])

    db_cursor.execute("SELECT * FROM states ORDER BY id")

    row_sellected = db_cursor.fetchall()

    for row in row_sellected:
        print(row)

    db_connect.commit()
    db_cursor.close()

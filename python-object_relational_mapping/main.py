import MySQLdb as DB

db_connect = DB.connect(host="localhost", port=3306,
                        user="root", passwd="mummysdaycjflute", db="cj")

db_cursor = db_connect.cursor()

# db_cursor.execute("SELECT * FROM infostudents")

# rows_selected = db_cursor.fetchall()

# for row in rows_selected:
#     print(row)

studentid = input("Student ID: ")
studentname = input("Student Name: ")
parentname = input("Parent Name: ")
studentaddress = input("Student Address: ")
postalcode = input("Postal Code: ")
city = input("City: ")

data = (studentid, studentname, parentname,
        studentaddress, postalcode, city)

value = ['StudentID', 'StudentName',
         'ParentName', 'Address', 'PostalCode', 'City']
count = 0

for i in data:
    db_cursor.execute(
        "INSERT INTO infostudents ({0})VALUES (%s)".format(value[count]), [i])
    count += 1
# db_cursor.execute(
#     "INSERT INTO infostudents (StudentID, StudentName, ParentName, Address, PostalCode, City) VALUES (%s)",
#     [data])
db_connect.commit()
# rows_selected = db_cursor.fetchall()


# for row in rows_selected:
#     print(row)


db_cursor.close()
# DB.close()

import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "alex",
password = "",
database="testdb"
)
mycursor = mydb.cursor()
mycursor.execute('select * from students where name like "%eff%"' )
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

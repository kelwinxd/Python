import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root8",
    database="testdb",
    port=3306

)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)






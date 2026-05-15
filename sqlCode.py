from os import name

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="test")
cursor = mydb.cursor()

cursor = mydb.cursor()
name =  str(input("Enter your name: "))
college = str(input("Enter your college name: "))
cursor.execute("Insert into student values(%s,%s)",(name,college))
cursor.execute("select * from student")

for x in cursor:
    print(x)

mydb.close()

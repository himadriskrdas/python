import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="test")
curs = mydb.cursor()
for x in curs:
    print(x)
a = str(input("Want to add a student (y/n) ? "))
if a == "y" :
        name =  str(input("Enter your name: "))
        college = str(input("Enter your college name: "))
        curs.execute("Insert into student values(%s,%s)",(name,college))
        curs.execute("select * from student")
else :
        print("Nothing to add: !!")
for x in curs:
    print(x)
mydb.commit()

action = str(input("Enter your action: "))
if action == "delete" or action == "remove" or action == "del" :
        name=str(input("Enter your name: "))
        curs.execute("delete from student where name = %s",name)
else :
        print("Not a valid action !! Thank You !!")
for x in curs:
    print(x)
mydb.close()

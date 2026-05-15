import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="test")
curs = mydb.cursor()

a = str(input("Want to add a student (y/n) ? "))
if a == "y" :
        name =  str(input("Enter your name: "))
        college = str(input("Enter your college name: "))
        curs.execute("Insert into student values(%s,%s)",(name,college))
        curs.execute("select * from student")
        for x in curs:
            print(x)
else :
        print("Nothing to add: !!")
        curs.execute("select * from student")
        for x in curs:
            print(x)



action = str(input("Enter your action: "))
if action == "delete" or action == "remove" or action == "del" :
        name=str(input("Enter your name: "))
        curs.execute("delete from student where name = %s",(name,))
        curs.execute("select * from student")
        for x in curs:
            print(x)
else :
        print("Not a valid action !!! Thank You !!!!")
mydb.commit()
mydb.close()

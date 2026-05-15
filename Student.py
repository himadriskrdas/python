class Student:
    def __init__(self,name,age,rollnumber,marks):
        self.Marks = marks
        self.name = name
        self.age = age
        self.rollnumber = rollnumber


    def show(self):
        print(self.name)
        print(self.age)
        print(self.rollnumber)
        print(self.Marks.total)


    class Marks:
        def __init__(self,total):
            self.total = 578

m1 = Student.Marks(600)
m2 = Student.Marks(578)
s1 = Student("Himadri",27,2,m1.total)
s2 = Student("Tuhin",27,1,m2.total)

s1.show()
s2.show()


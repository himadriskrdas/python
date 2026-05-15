from os import name


class Computer:

    def __init__(self):
        self.name= "Himadri"
        self.age =29
    def update(self):
        self.age =37
    def Compare(self,otherobj):
        if self.age == otherobj.age:
            print("Age is same: Same object")
        else:
            print("Age is different: Different object")
c1 = Computer()
c2 = Computer()

c1.Compare(c2)
print(c1.age)
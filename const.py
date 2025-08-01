class Student:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def display(self):
        print(f'Hi {self.name},Your age is {self.age}')

s1=Student('Pradeep',20)
s1.display()
s2=Student('Elaks',20)
s2.display()

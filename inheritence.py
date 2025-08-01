#main use of inehritence is the reuse of code 

class dad:
    def house(self):
        print("Red")

class son(dad):
    def fact(self):
        print("I am from fact")
    def house(self):
        print("Purple")
d1=dad()
print("I am dad and my house is")
d1.house()
s=son()
print("I am his son and ")
s.fact()
print("I repainted the house color in ")
s.house()

 
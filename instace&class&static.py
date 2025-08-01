class Employees:
    company="Carvo"
    @classmethod
    def change_company(cls,newname):
        cls.company=newname
    @staticmethod
    def try_change_name(newname):
        company=newname
print("Old Name:",Employees.company)

Employees.change_company("Void Games")
print("Updated Name:",Employees.company)

Employees.try_change_name("Meta")
print("2nd Updated Name:",Employees.company) 
        

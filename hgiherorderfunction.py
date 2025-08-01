def domain(mail):
    def name(name):
        return f"{name}@{mail}"
    return name
mail1=domain("gmail.com")
mail2=domain("yahoo.com")
mail3=domain("carvo.com")

print(mail1("pradeep"))
print(mail2("pradeep"))
print(mail3("pradeep"))
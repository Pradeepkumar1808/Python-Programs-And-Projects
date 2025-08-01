def greeting(msg):
    def name():

        return f"{msg}"
    return name

namer=greeting("Pradeep")
print(namer())
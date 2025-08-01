#this is for writting file

'''file=open("file.txt","w")

file.write("Hello Pradeep\n")

file.write("Welcome to my channel\n")

file.write("update\n")

file.close() '''
#this is fro reading file
'''
file=open("file.txt","r")

content=file.read()
print("File Content:",content)

file.close()

'''
# this is appending means adding contents to the file
'''
file=open("file.txt","a")
file.write("This is a appended line")
file.close()
'''
#now i will open this file and print in short way
'''
with open("file.txt","r") as file:
    for line in file:
        print(line.strip())'''
'''
feedback=input("Enter your Feedback here Please")
with open("file.txt","w") as log:
    log.write(feedback+'\n')
print("Thanks For your Feedback")
'''

with open ("file.txt") as line1:
    while True:
        line=line1.readline()
        print(line.strip())
        if not line:
            break 
        if "bitch" in line:
            print("Curse Word Found",line.strip())
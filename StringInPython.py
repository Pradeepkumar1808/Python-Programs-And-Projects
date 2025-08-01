#String are also Known as array

#Retrieving a character from a String
print(f"Retrieving a Character From a String")
a="Putin_ser"
print(a[1])
#OP is "u"

#looping through String
print(f"Looping through a string")
for i in 'Pradeep Kumar ':
    print(i)

#Reversing a string 
print(f"Reversing A String")
rev=" "
for x in "Pradeep Kumar":
    rev= x + rev
print(rev)

#slicing a string 
print(f"String Slicing")
k="Hallow Sar"
print(k[2:8])

#Modify String
#Uppercase()&& Lowercase && Strip && Replacing & Split

name=" Pradeep Kumar"
print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace('d','v').replace('p','n'))
print(name.split())
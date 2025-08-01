#let's create a list first

friend=['elaks','kishore','bhuvanesh','vishva','sanjeevi','varun']
print("Original List:",friend)
#lets now use list methods on this list

#list append
friend.append('Kerthi')
print("Append:",friend)

#list insert

friend.insert(1,'Vedi Muthu')
print("After Insert",friend)

#list remove

friend.remove("vishva")
print("List After Remove:",friend)

#list pop
friend.pop()
print("List After Pop:",friend)

#list reverse
friend.reverse()
print("Lsit after Reverse:",friend)

#list count
print("Count:",friend.count('elaks'))

#list slice
print("Top 5",friend[0:2])

#list iteration

for i in friend:
    print("This is my friend",i)

#check if 
if 'elaks' in friend:
    print("Yes")

#update
friend[1]='Kerthi'
print(friend)

 
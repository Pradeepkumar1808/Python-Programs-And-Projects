print('Enter Total number of subjects')
n=int(input())
print("Enter the Marks as follow")
totmarks=0
for i in range(n):
    marks=int(input())
    totmarks += marks
avg=totmarks/n

if avg>35:
    print("Eligible")
else:
    print("Not Eligible")
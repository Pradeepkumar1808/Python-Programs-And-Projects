import matplotlib.pyplot as plt
import csv
'''
x=[1,2,3,4]
y=[12,13,14,30]

plt.plot(x,y)
plt.title("Graph")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()'''
'''
x=['Banana','Grapes','Apple']
y=[12,32,56]

plt.bar(x,y,color='Green')
plt.title('Fruits')
plt.ylabel('Count')
plt.show()

'''
'''
x=[1,2,3,4]
y=[12,13,14,30]
plt.scatter(x,y,color='Red')
plt.title("Graph")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
'''
'''
month=[]
sales=[]

with open('monthlysales.csv','r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        month.append(row['month'])
        sales.append(int(row['sales']))

plt.plot(month,sales,marker='o')
plt.title('Sales Visualization')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
'''
employees ={
    'Game_dev':'Bhuvanesh',
    'Front-end_Dev':'Kishore',
    'Data Analyst':'Elaks',
    'Data_Engineer':'Putin'

}
employees.update({"Designer":"Varun Putin"})
print(employees.keys())
print(employees.values())

for key,value in employees.items():
    print(key,':',value)



customrs_order={
    'OR001':{'order_id':'OR004','cus_name':'Elakkyan','gender':'Sigma-male','age':'30'},
    'OR002':{'order_id':'OR004','cus_name':'Varun','gender':'boi','age':'10'},
    'OR003':{'order_id':'OR004','cus_name':'Bhuvanesh','gender':'They/them','age':'40'},
    'OR004':{'order_id':'OR004','cus_name':'Kishore','gender':'Preferred not to say','age':'?'}
    
    }

for order_id,gender_desc in customrs_order.items():
    print(order_id)
    print(gender_desc['cus_name'],'->',gender_desc['gender'])
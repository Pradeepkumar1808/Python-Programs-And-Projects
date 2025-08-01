print("Exception Handling")
'''
a=2
b=0
try:

    print(a/b,end=" ")
except:
    print("Error")
'''
try:
    number_of_items=int(input("Enter Your No of Items"))
    total_Items=200*number_of_items
    avg_price=total_Items/number_of_items
except ZeroDivisionError:
    print("Error! No of items cannot be zero!!")
print("Thank you !")

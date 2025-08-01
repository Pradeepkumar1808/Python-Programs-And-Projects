"""
#Text type

a=str(input())
print(a,"=>",type(a)) #This is used for storing textutal data

#Numeric Type

b=int(input())
print(b,"=>",type(b))

c=complex(input())
print(c,"=>",type(c))

d=list(("Mango","Litchi","Cherry")) #Mutable Sequence
print(d,"=>",type(d))

e=tuple(("Mango","Litchi","Cherry")) #Immutable Sequence
print(e,"=>",type(e))

f=range(input())
print(list(f),"=>",type(f))
"""
#Now let's write a programt to showcase entered input's data type

user_input=input("Enter Something To Know It's DataType In Python!")

def check_value(value):
    try:
        int_val=int(value)
        print(f"You had entered a Integer")
        return
    except ValueError:
        pass

    try:
        float_val=float(value)
        print(f"You had Entered a Float",type(float_val))
        return
    except ValueError:
        pass

    if value.lower() == 'true' or value.lower() == 'false':
        bool_val = value.lower() == 'true'
        print(f"You had entered a boolean")
        return
    if value.startswith('[') and value.endswith(']'):
        try:
            list_val=eval(value)
            if isinstance(list_val, list):
                print(f"You had entered a List")
                return
        except:
            pass

    print(f"You entered a String: '{value}' =>", type(value))

check_value(user_input)
    

        

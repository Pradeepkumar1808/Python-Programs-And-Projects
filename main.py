user_input = input("Enter something: ")

# Try to detect the actual type
def detect_type(value):
    try:
        int_val = int(value)
        print(f"You entered an Integer: {int_val} =>", type(int_val))
        return
    except ValueError:
        pass

    try:
        float_val = float(value)
        print(f"You entered a Float: {float_val} =>", type(float_val))
        return
    except ValueError:
        pass

    if value.lower() == 'true' or value.lower() == 'false':
        bool_val = value.lower() == 'true'
        print(f"You entered a Boolean: {bool_val} =>", type(bool_val))
        return

    if value.startswith('[') and value.endswith(']'):
        try:
            list_val = eval(value)
            if isinstance(list_val, list):
                print(f"You entered a List: {list_val} =>", type(list_val))
                return
        except:
            pass

    print(f"You entered a String: '{value}' =>", type(value))

# Call the function
detect_type(user_input)

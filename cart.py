items=[]

while True:
    item=input("Enter the Grocery Items(Type Done to Exit)")
    if item.lower()=="done":
        break
    items.append(item)
print(f"Items Inside Your Cart: {items}")

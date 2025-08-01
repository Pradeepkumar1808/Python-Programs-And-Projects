import pandas as pd

df=pd.read_csv("sales_data.csv")

df['total']=df['price']*df['quantity']
grouped=df.groupby('product')['total'].sum().reset_index()

sorted_data=grouped.sort_values(by='total' ,ascending=False)

print("Sorted Data")
print(sorted_data)
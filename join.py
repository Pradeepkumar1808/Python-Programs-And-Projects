import pandas as pd

first_data=pd.DataFrame({
    'Customer_id' : [1,2,3,4],
    'Name': ['Varun','Pradeep','Kishore','Elaks']
})

second_data=pd.DataFrame({
    'order': [101,202,321,123],
    'Customer_id' : [1,2,3,4],
    'Product': ['Shoes','Caps','Headphone','Connector']
})

merge=pd.merge(first_data,second_data,on='Customer_id',how='outer')
print(merge)
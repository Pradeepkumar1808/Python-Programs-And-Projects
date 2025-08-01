import pandas as pd
import numpy as np

df=pd.DataFrame({
    'Name':['Praeep','Varun','bones'],
    'Relation':['Daddy','Son','Uncle']


})
print(np.where(df['Relation']=='Daddy'),''
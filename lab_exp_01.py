import pandas as pd
technologies={
    'Course':["Python","Pyspark","Hadoop","AWS","Azure"],
    'Fees' : [1000,2000,5000,6000,15000],
    'Duration' : ["10 days","5 days","15 days","7 days","3 days"],
    'Discount' : [100,200,500,600,1500]

}

df=pd.DataFrame(technologies)

print("Data Frame:")
print(df)
print()
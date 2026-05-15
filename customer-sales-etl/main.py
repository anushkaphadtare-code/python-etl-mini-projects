import pandas as pd

#df= pd.read_csv('sample_data.csv')

#print(df.head())
#print(df.info())
#print(df.isnull())

#print(df.isnull().sum())

#df['sales']=df['sales'].fillna(0)

#df['sales_with_tax'] = df['sales'] * 1.18

#print(df)

#df.to_csv('cleaned_data.csv', index = False)

df1 = pd.read_csv('cleaned_data.csv')


df1['customer_name_upper'] = df1['customer_name'].str.upper()
print(df1)

high_sales = df1[df1['sales'] > 5000]
print(high_sales)

total_sales = df1['sales'].sum()
print(total_sales)

df2 = df1.sort_values(by = 'sales', ascending = False)
print(df2)

df1.to_csv('more_transformations.csv', index = False)
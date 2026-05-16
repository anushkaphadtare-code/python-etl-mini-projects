import pandas as pd

df=pd.read_csv('cleaned_data.csv')
print(df)

# Inspect data:
print(df.head())
print(df.info())

# Filtering:
high_sales = df[df['sales'] > 5000]
print(high_sales)

# Sorting:
sorted_df = df.sort_values(by = 'sales', ascending = False)
print(sorted_df)

# Grouping: total sales by city:
city_sales = df.groupby('city')['sales'].sum()
print(city_sales)

# Aggregations: 
# 1) Total sales:
print("The total sales are: ",df['sales'].sum())
# 2) Mean sales:
print("Avg sales are: ",df['sales'].mean())
# 3) Maximum sales:
print("Maximum sales are: ",df['sales'].max())

city_sales.to_csv('city_wise_sales_summary.csv', index = False)

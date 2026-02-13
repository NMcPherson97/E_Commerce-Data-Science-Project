import pandas as pd
import numpy as np
import datetime as dt
import matplotlib as plt

sales_data = pd.read_csv('ecommerce_sales_data.csv')

#Total sales by category
category_sales = sales_data.groupby('Category')['Sales'].sum()
# print(category_sales)

#Total profit by category
category_profit = sales_data.groupby('Category')['Profit'].sum()
# print(category_profit)

#Profit margin column creation
sales_data['Profit_Margin'] = sales_data['Profit'] / sales_data['Sales']

#Profit per unit column creation
sales_data['Profit_Per_Unit'] = sales_data['Profit'] / sales_data['Quantity']

#date column conversion and quarter column creation
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
sales_data['MM-DD'] = sales_data['Order Date'].dt.strftime('%m-%d')

#Rename 'MM-DD' to 'Quarter' and convert datatype
sales_data = sales_data.rename(columns = {'MM-DD':'Quarter'})
sales_data['Quarter'] = sales_data['Quarter'].str.replace('-','.').astype('float')
print(sales_data['Quarter'])



#quarterly tables
# quarter1 = sales_data[(sales_data['Quarter'] >= 1) & (sales_data['Quarter'] < 4)].reset_index()
# quarter2 = sales_data[(sales_data['Quarter'] >= 4) & (sales_data['Quarter'] < 6)].reset_index()
# quarter3 = sales_data[(sales_data['Quarter'] >= 6) & (sales_data['Quarter'] < 9)].reset_index()
# quarter4 = sales_data[(sales_data['Quarter'] >= 9) & (sales_data['Quarter'] < 12)].reset_index()
# print(quarter1)
# print(quarter2)
# print(quarter3)
# print(quarter4)





#regional tables
north_df = sales_data[sales_data.Region == 'North'].reset_index()
# print(north_df)

south_df = sales_data[sales_data.Region == 'South'].reset_index()

east_df = sales_data[sales_data.Region == 'East'].reset_index()

west_df = sales_data[sales_data.Region == 'West'].reset_index()

#Best and worst performing products in each region
north_category_sales = north_df.groupby(['Product Name', 'Category']).Sales.sum().sort_values(ascending=False)
# print(north_category_sales)

south_category_sales = south_df.groupby(['Product Name', 'Category']).Sales.sum().sort_values(ascending=False)

east_category_sales = east_df.groupby(['Product Name', 'Category']).Sales.sum().sort_values(ascending=False)

west_category_sales = west_df.groupby(['Product Name', 'Category']).Sales.sum().sort_values(ascending=False)


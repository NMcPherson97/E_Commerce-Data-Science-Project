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
month_day = pd.to_datetime(sales_data['MM-DD'])
sales_data['Quarter'] = month_day.dt.quarter
print(sales_data.head(10))


#quarterly tables






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


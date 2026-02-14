import pandas as pd 
import numpy as np 
import datetime as dt 
import matplotlib as plt 
sales_data = pd.read_csv('ecommerce_sales_data.csv') 
#Total sales by category 
category_sales = sales_data.groupby('Category')['Sales'].sum() 
# print(category_sales) 
# #Total profit by category 
category_profit = sales_data.groupby('Category')['Profit'].sum() 
# print(category_profit) 
# #Profit margin column creation 
sales_data['Profit_Margin'] = sales_data['Profit'] / sales_data['Sales'] 
#Profit per unit column creation 
sales_data['Profit_Per_Unit'] = sales_data['Profit'] / sales_data['Quantity'] 
#date column conversion and quarter column creation 
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date']) 
sales_data['Quarter'] = sales_data['Order Date'].dt.quarter 
#quarterly tables 
quarter1 = sales_data[sales_data['Quarter'] == 1].reset_index() 
quarter2 = sales_data[sales_data['Quarter'] == 2].reset_index() 
quarter3 = sales_data[sales_data['Quarter'] == 3].reset_index() 
quarter4 = sales_data[sales_data['Quarter'] == 4].reset_index() 
#Best and worst performing products by quarter 
quarter1_sales = quarter1.groupby(['Product Name', 'Category']).Sales.sum.sort_values(ascending=False) 
quarter2_sales = quarter2.groupby(['Product Name', 'Category']).Sales.sum.sort_values(ascending=False) 
quarter3_sales = quarter3.groupby(['Product Name', 'Category']).Sales.sum.sort_values(ascending=False) 
quarter4_sales = quarter4.groupby(['Product Name', 'Category']).Sales.sum.sort_values(ascending=False) 
#regional tables 
north_df = sales_data[sales_data.Region == 'North'].reset_index() 
south_df = sales_data[sales_data.Region == 'South'].reset_index() 
east_df = sales_data[sales_data.Region == 'East'].reset_index() 
west_df = sales_data[sales_data.Region == 'West'].reset_index() 

# #Best and worst performing products in each region 
north_category_sales = north_df.groupby(['Product Name', 'Category']).Sales.sum().sort_values(ascending=False) 
south_category_sales = south_df.groupby(['Product Name', 'Category']).Sales.sum().sort_values(ascending=False) 
east_category_sales = east_df.groupby(['Product Name', 'Category']).Sales.sum().sort_values(ascending=False) 
west_category_sales = west_df.groupby(['Product Name', 'Category']).Sales.sum().sort_values(ascending=False)
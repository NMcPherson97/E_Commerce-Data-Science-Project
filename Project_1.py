import pandas as pd 
import numpy as np 
import datetime as dt 
import matplotlib as plt 
sales_data = pd.read_csv('ecommerce_sales_data.csv') 
#Total sales by category 
category_sales = sales_data.groupby('Category')['Sales'].sum() 

# #Total profit by category 
category_profit = sales_data.groupby('Category')['Profit'].sum() 

# #Profit margin column creation 
sales_data['Profit_Margin'] = sales_data['Profit'] / sales_data['Sales'] 

#Profit per unit column creation 
sales_data['Profit_Per_Unit'] = sales_data['Profit'] / sales_data['Quantity']

#date column conversion and quarter column creation 
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date']) 
sales_data['Quarter'] = sales_data['Order Date'].dt.quarter 


#quarterly tables 
quarter_sales = (
    sales_data
    .groupby(['Quarter', 'Product Name', 'Category'])['Sales']
    .sum()
    .sort_values(ascending=False)
)

#regional tables 
region_sales = (
    sales_data
    .groupby(['Region', 'Product Name', 'Category'])['Sales']
    .sum()
    .sort_values(ascending=False)
)

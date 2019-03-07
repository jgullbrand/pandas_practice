# Pandas Multiple Tables

import pandas as pd

# Loading in data from 3 tables: Total Website Visitors, New Visitors, Avg Session Duration

total_visitors = pd.read_csv('visitors.csv')
new_visitors = pd.read_csv('new_visitors.csv')
session_duration = pd.read_csv('session_duration.csv')

# Check out dataframes:
#print(total_visitors)
#print(new_visitors)
#print(session_duration)


# Inner Merge

# Can merge two tables with pd.merge (identifies matching column automatically)
all_visitor_data = pd.merge(total_visitors, new_visitors)

#Add a new visitor column - what % of total visitors were new visitors?
all_visitor_data['New Visitors Percentage'] = round(all_visitor_data.new_website_visitors / all_visitor_data.total_website_visitors,2)


# Merging all three tables - you can do this by "chaining" commands:
all_data = total_visitors.merge(new_visitors).merge(session_duration)

#Rename column header from 'Session Duration' to 'session_duration'
all_data.rename(columns={'Session Duration':'session_duration'}, inplace = True)

#Filter -only show data where 'session_duration' is over 15 seconds
long_avg_session_duration = all_data[all_data.session_duration > 15]


#-------
#Looking at two new data files. Customer info + Website Sales

customers = pd.read_csv('customers.csv')
website_sales = pd.read_csv('website_sales.csv')

#print(customers)
#print(website_sales)

#Merge on columns when the names don't match. Use left_on and right_on:
customer_sales_data = pd.merge(customers, website_sales, 
							   left_on='id', right_on='customer_id')

#print(customer_sales_data)
# Printing this data shows 1) It renamed the two id columns id x & id y
# and 2) it removed the row that we didn't have a matching customer id for

# Let's rename the id columns and keep all data by using an 'outer join'
all_customer_sales_data = pd.merge(customers, website_sales, 
							   left_on='id', right_on='customer_id',
							   how = 'outer',
							   suffixes=['_customers', '_sales'])
#print(all_customer_sales_data)

# view only rows with null sales data
null_sales_data = all_customer_sales_data[all_customer_sales_data.total_sales.isnull()]
# Count the number of rows with null sales data
count_null_sales_data = len(null_sales_data)

# left merge
customer_data_left_merge = pd.merge(customers, website_sales, 
							   left_on='id', right_on='customer_id',
							   how = 'left',
							   suffixes=['_customers', '_sales'])

#print(customer_data_left_merge)

# right merge
customer_data_left_right = pd.merge(customers, website_sales, 
							   left_on='id', right_on='customer_id',
							   how = 'right',
							   suffixes=['_customers', '_sales'])

#print(customer_data_left_right)


#-------
#Concatenate DataFrames

customers = pd.read_csv('customers.csv')
customers_two = pd.read_csv('customers_two.csv')

combined_customer_data = pd.concat([customers, customers_two]).reset_index(drop=True)
print(combined_customer_data)



import pandas as pd
import numpy as np


#loading data from this csv file and saving it to the variable df
df = pd.read_csv('eyecenter_data.csv')
#print(df)

#head() method gives first 5 rows by default
first_five_rows = df.head()

#shows first 10 rows
first_five_rows = df.head(10)

#Gives statistics for each column
#column_info = df.info()

#print data for a specific column. Two different ways of executing to get the same data:
column_data = df.email
column_data2 = df['email']

# need to use two sets of brackets
select_multiple_columns = df[['first_name', 'last_name', 'email']]
#print(select_multiple_columns)

#select a single row of data using iloc. Based on zero-index.
select_one_row = df.iloc[0]
#print(select_one_row)

# this will select the first three rows
select_multiple_rows = df.iloc[0:3]
#print(select_multiple_rows)

#filter data based on if someone is younger than 30
select_subset_age = df[df.age < 30]
select_subset_contacts = df[df.contacts_or_eyeglasses == 'contacts']
select_subset_eyeglasses = df[df.contacts_or_eyeglasses == 'eyeglasses']
select_subset_none = df[df.contacts_or_eyeglasses == 'none']

# or
select_subset_or = df[(df.age >40) | (df.contacts_or_eyeglasses == 'eyeglasses')]

# and
select_subset_and = df[(df.first_name == 'Jamie') & (df.last_name == 'Gullbrand')]

# isin command is used to identify & display a list of values in a column
isin_name = df[df.first_name.isin(['Jamie', 'Judy', 'Timothy'])]
#print(isin_name)

# Check to see if a specific columns contains a piece of a string, filters to show relevant rows of data.
contains_data = df[df['contacts_or_eyeglasses'].str.contains("glas")]
#print(contains_data)

# print to a csv only columns that contain a piece of a string 'Jam' in a first name. 
def print_name():
	data_name_contains = df[df['last_name'].str.contains("kins")]
	data_name_contains.to_csv('output_name_contains.csv')	

# practice resetting indices. Using [[]] when filtering multiple rows
df2 = df.iloc[[1,3,5]]
# resets index
reset_index_df2 = df2.reset_index()

# remove old index as a new column using drop = True.
# you can also modify an existing data frame rather than creating a new one using inplace=True
df2.reset_index(inplace=True, drop=True) 
#print(df2)

# to_csv() method saves csv file in current directory
#df.to_csv('output.csv')

# Add a column - specific data for each row. This would append the column to the existing data set.
df['customer_number'] = [2,32,49,78,82,99,103,109,201,250]

# Add a column - same data for all rows.
df['current_customer'] = 'Yes'
df['age_discount'] = .80 # 20% off
df['eye_exam_cost'] = 150

# Add a column based on performing a function on existing data. Age 10 years ago
df['age_ten_years_ago'] = df['age'] -10

def exclamation (string):
	return string + "!!!"

def uppercase (string):
	return string.upper()	

# Using the Apply function to apply a function to every value in the column. 
df['Excited Name!'] = df.first_name.apply(exclamation)
df['UPPERCASE NAME'] = df.first_name.apply(uppercase)


# LAMBDA EX 1: Using the lambda function on a column
get_first_initial = lambda x: x[0]
df['first_initial'] = df.first_name.apply(get_first_initial)

# LAMBDA EX 2: check if someone is older than 65
df['Older than 65?'] = df.age.apply(lambda x: True \
if x > 65 else False)

# LAMBDA EX 3: Using lambda on multiple columns at once by taking in an 'entire row'
get_total_cost = lambda row: row['eye_exam_cost'] * row['age_discount'] \
if row['age'] > 65 else row['eye_exam_cost']

df['Total Price including age discount if older than 65']  = df.apply(get_total_cost, axis =1)

# LAMBDA EX 4: Another example of taking in data from across a full row:
df['customer_basic_info'] = df.apply(lambda row: "Full Name: {} {}, Email: {}, Age: {}"\
    .format(row.first_name,
            row.last_name,
            row.email,
            row.age),
    axis=1)


# Can change all of the columns name at once by setting .columns = to an updated list
#df.columns = ['Column1 Name', 'Column2 Name']

# Change columns name for specific columns. inplace=True lets us edit the original DataFrame
df.rename(columns={
	'email': 'EMAIL ADDRESS'
	}, inplace = True)

df.rename(columns={
	'first_name': 'FIRST NAME',
	'last_name': 'LAST NAME',
	}, inplace = True)

#----------------------------
# Pandas Aggregates 

# basic functions with the data in the ages column
#print(df.age) 
print("Mean: {}".format(df.age.mean()))
print("Median: {}".format(df.age.median()))
print("Standard Deviation: {}".format(df.age.std()))
print("Max Number: {}".format(df.age.max()))
print("Min Number: {}".format(df.age.min()))
print("Count Values in Column: {}".format(df.age.count()))
print("Number of unique values: {}".format(df.age.nunique()))
print("List of unique values: {}".format(df.age.unique()))


# groupby method in pandas allows you to calculate based on groups of data
# In this example, I'm grouping by city and looking at the average age. Should print totals for Portland, Buxton, Boston.
age_by_city = df.groupby('location_city').age.mean()
print("Grouped average ages by city: {}".format(age_by_city))

vision_insurance = df.groupby('vision_insurance').customer_number.count()
print("# of people with / without vision insurance: {}".format(vision_insurance))
print(type(vision_insurance)) # Series

# Using reset_index at the end will transform the type Series into a DataFrame
vision_insurance = df.groupby('vision_insurance').customer_number.count().reset_index()
print("# of people with / without vision insurance: {}".format(vision_insurance))
print(type(vision_insurance)) # DataFrame - because we added .reset_index()

# Calculating percentiles using numpy with a lambda function
age_percentiles = df.groupby('location_city').age.apply(lambda x: np.percentile(x,75)).reset_index()
print('75th percentile of age for each city')
print(age_percentiles)


#df.pivot(columns='ColumnToPivot',
#         index='ColumnToBeRows',
#         values='ColumnToBeValues')


#print(df)
#df.to_csv('output.csv')


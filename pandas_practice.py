import pandas as pd

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
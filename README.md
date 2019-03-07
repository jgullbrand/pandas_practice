##**Pandas Practice - loading & analyzing data in a single table**

I created a table of data in a csv file that models an eye center. Here's what eyecenter_data.csv looks like: 

| first_name | last_name | age | email                     | location_city | location_state | contacts_or_eyeglasses | vision_insurance | 
|------------|-----------|-----|---------------------------|---------------|----------------|------------------------|------------------| 
| Jamie      | Gullbrand | 25  | jamie.gullbrand@email.com | Boston        | Massachusetts  | none                   | yes              | 
| Zach       | Tomkins   | 29  | zach@email.com            | Portland      | Maine          | contacts               | no               | 
| Adam       | Jones     | 21  | adamjones@email.com       | Portland      | Maine          | eyeglasses             | no               | 
| Mookie     | Betts     | 26  | mookie@sox.com            | Boston        | Massachusetts  | none                   | yes              | 
| Tom        | Gardiner  | 29  | tom@email.com             | Portland      | Maine          | contacts               | no               | 
| Grant      | Gardiner  | 35  | grant@email.com           | Portland      | Maine          | contacts               | no               | 
| Timothy    | Gardiner  | 37  | timothy@email.com         | Portland      | Maine          | contacts               | no               | 
| Alex       | Cora      | 45  | alex@sox.com              | Boston        | Massachusetts  | contacts               | yes              | 
| Judy       | Alison    | 69  | judy@email.com            | Buxton        | Maine          | eyeglasses             | yes              | 
| Jerry      | Alison    | 72  | jerry@email.com           | Buxton        | Maine          | eyeglasses             | no               | 

With this table of data, I practiced functionality of pandas including: 
- Reading data from a CSV with read_csv() and printing with to_csv()
- Previewing the data set with head() and info()
- Selecting certain columns / rows of data based on specified criteria
- Filtering rows that equal a certain value or that contain a string
- Using apply() and lambda to apply functions across rows of data
- Calculting the mean, median, standard deviation, max/min, count, # unique values
- Using groupby() to apply calculations to collections of the data.


##**Pandas Practice - Working with multiple tables**

I created three separate tables that show website analytics: visitors.csv, new_visitors.csv, session_duration.csv: 

| Month     | total_website_visitors |  | Month     | new_website_visitors |  | Month     | Session Duration | 
|-----------|------------------------|--|-----------|----------------------|--|-----------|------------------| 
| January   | 353                    |  | January   | 32                   |  | January   | 17               | 
| February  | 353                    |  | February  | 32                   |  | February  | 12               | 
| March     | 279                    |  | March     | 104                  |  | March     | 10               | 
| April     | 336                    |  | April     | 32                   |  | April     | 16               | 
| May       | 268                    |  | May       | 31                   |  | May       | 9                | 
| June      | 267                    |  | June      | 50                   |  | June      | 17               | 
| July      | 358                    |  | July      | 113                  |  | July      | 2                | 
| August    | 244                    |  | August    | 121                  |  | August    | 3                | 
| September | 360                    |  | September | 124                  |  | September | 8                | 
| October   | 305                    |  | October   | 69                   |  | October   | 3                | 
| November  | 270                    |  | November  | 77                   |  | November  | 20               | 
| December  | 328                    |  | December  | 55                   |  | December  | 4                | 

 With these tables, I practiced functionality of pandas including:
 - Using pd.merge to merge a couple of the tables (automatically based on the month column)
 - Merging all of the tables by chaining the commands
 - Renaming columns to make it easier to merge / manage
 - Practiced the following types of merges: Inner, Outer, Left, Right, Concatenating

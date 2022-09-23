#Numpy

# Below is information about selected columns from the dataset:

#pickup_year: the year of the trip
#pickup_month: the month of the trip (January is 1, December is 12)
#pickup_day: the day of the month of the trip
#pickup_
ation_code: the airport or borough where the the trip started
#dropoff_location_code: the airport or borough where the the trip finished
#trip_distance: the distance of the trip in miles
#trip_length: the length of the trip in seconds
#fare_amount: the base fare of the trip, in dollars
#total_amount: the total amount charged to the passenger, including all fees, tolls and tips#

#convert a list of a lists in ndarray
import numpy as npf = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))
taxi = np.array(taxi_list)

# But what if we want to find the maximum value of each row? We need to 
#use the axis parameter and specify a value of 1 to indicate that we want to calculate the maximum value for each row.

# we'll compare against the first 5 rows only
taxi_first_five = taxi[:5]
# select these columns: fare_amount, fees_amount, tolls_amount, tip_amount
fare_components = taxi_first_five[:,9:13]

# calculate the sum of each row in fare_components
fare_sums = fare_components.sum(axis=1)

# extract the 14th column in taxi_first_five
fare_totals = taxi_first_five[:,13]

print(fare_totals)
print(fare_sums)

#output
[ 69.99   54.3   37.8  32.76   18.8]
[ 69.99   54.3   37.8  32.76   18.8]

# numpy - booleans array

# operation
print(np.array([2,4,6,8]) + 10)
#output
[12 14 16 18]

print(np.array([2,4,6,8]) < 5)
#output
[ True  True False False]

#booleans
a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = a < 3
b_bool = b == 'blue'
c_bool = c > 100

print(a_bool)
#output
[ True  True False False False]

#example to index a boolean
#Let's use Boolean indexing to confirm the number of taxi rides in our data set from the month of January. 
pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

print(january_rides)
#output
800
# There are 800 rides in our dataset from the month of January. 

#example 02
pickup_month = taxi[:,1]

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

print(february_rides)
#Output
176

# example 03

# create a boolean array for trips with average
# speeds greater than 20,000 mph
trip_mph_bool = trip_mph > 20000

# use the boolean array to select the rows for
# those trips, and the pickup_location_code,
# dropoff_location_code, trip_distance, and
# trip_length columns
trips_over_20000_mph = taxi[trip_mph_bool,5:9]

print(trips_over_20000_mph)

[[     2      2     23      1]
 [     2      2   19.6      1]
 [     2      2   16.7      2]
 [     3      3   17.8      2]
 [     2      2   17.2      2]
 [     3      3   16.9      3]
 [     2      2   27.1      4]]

# example 04

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()

# modifie the row index 1066 and the column index 5
taxi_modified[1066,5] = 1
#Use assignment to change these values to the YY format (16)
taxi_modified[:,0] = 16
#The values at column index 7 (trip_distance) of rows index 550 and 551 are incorrect. Use assignment to change these values in the taxi_modified ndarray to the mean value for that column
taxi_modified[550:552, 7] = taxi_modified[:,7].mean()


# challenge nparray 01
# To complete this task, we'll need to check if the dropoff_location_code column (column index 6) is equal to one of the following values:

2: JFK Airport
3: LaGuardia Airport
5: Newark Airport.

# 01
jfk_booltaxi = taxi[:, 6] == 2

jfk = taxi[jfk_booltaxi]

shape1 = taxi.shape
shape2 = jfk.shape

jfk_count = len(jfk)

# 02
laguardia_booltaxi = taxi[:, 6] == 3

laguardia = taxi[laguardia_booltaxi]

laguardia_count = len(laguardia)

# 03
newark_booltaxi = taxi[:, 6] == 5

newark = taxi[newark_booltaxi]

newark_count = len(newark)

#04
print(jfk_count)
print(laguardia_count)
print(newark_count)

#outlook
285
308
2

# challenge 02

#We'll start by using Boolean indexing to remove any rows that have an average speed for the trip greater than 100 mph (160 kph) 
#which should remove any questionable data. Then, we'll use array methods to calculate the mean for specific columns of the remaining data. 
#Here are the columns we're interested in:

trip_distance, at column index 7
trip_length, at column index 8
total_amount, at column index 13

#01
cleaned_taxi_bool = trip_mph < 100
cleaned_taxi = taxi[cleaned_taxi_bool]

shape1 = taxi.shape
shape2 = cleaned_taxi.shape

#02
mean_distance = np.mean(cleaned_taxi[:,7]) 
mean_length = np.mean(cleaned_taxi[:,8]) 
mean_total_amount = np.mean(cleaned_taxi[:,13]) 

########################################################################

# INTRODUCTION TO PANDAS

#head - first 6 rows
f500_head = f500.head(6)

#tail - last 8 rows
f500_tail = f500.tail(8)

print(f500_head)

print(f500_tail)
-------

# return information about the types of each column.
print(f500_selection.dtypes)

#output
rank          int64
revenues      int64
profits     float64
country      object
dtype: object

#You may recognize the float64 dtype from our work in NumPy. Pandas uses NumPy dtypes for numeric columns, including integer64. 
#There is also a type we haven't seen before, *object*, which is used for columns that have data that doesn't 
#fit into any other dtypes. This is normally used for columns containing string values

f500.info()

#Output
<class 'pandas.core.frame.DataFrame'>
Index: 500 entries, Walmart to AutoNation
Data columns (total 16 columns):
rank                        500 non-null int64
revenues                    500 non-null int64
revenue_change              498 non-null float64
profits                     499 non-null float64
assets                      500 non-null int64
profit_change               436 non-null float64
ceo                         500 non-null object
industry                    500 non-null object
sector                      500 non-null object
previous_rank               500 non-null int64
country                     500 non-null object
hq_location                 500 non-null object
website                     500 non-null object
years_on_global_500_list    500 non-null int64
employees                   500 non-null int64
total_stockholder_equity    500 non-null int64
dtypes: float64(3), int64(7), object(6)
 
 # Select the industry column and assign the result to the variable name industries.
 industries = f500["industry"]
 
 # loc
 df.loc[row_label, column_label]
 
 # 1d pandas = serie object
 # 2d pandas = dataframe
 
 # take a object in a dataframe
Select by Label	      Explicit Syntax	                   Common Shorthand
Single column	        df.loc[:,"col1"]	                  df["col1"]
List of columns	      df.loc[:,["col1", "col7"]]	        df[["col1", "col7"]]
Slice of columns	     df.loc[:,"col1":"col4"]	           -

# exercice 01

#select country column
countries = f500['country']
#select revenues and years_on_global_500_list columns
revenues_years = f500[['revenues', 'years_on_global_500_list']]
#select the column ceo up to sector
ceo_to_sector = f500.loc[:,'ceo':'sector']

# select a single row
single_row = f500_selection.loc["Sinopec Group"]
print(type(single_row))
print(single_row)

#output
class 'pandas.core.series.Series' # it's a series because it's a 1d pandas

rank             3
revenues    267518
profits     1257.9
country      China
Name: Sinopec Group, dtype: object
  
# select a list of rows
list_rows = f500_selection.loc[["Toyota Motor", "Walmart"]]
print(type(list_rows))
print(list_rows)

#output
class 'pandas.core.frame.DataFrame'

              rank  revenues  profits country
Toyota Motor     5    254694  16899.3   Japan
Walmart          1    485873  13643.0     USA

#For selection using slices, we can use the shortcut below. 
#This is the reason we can't use this shortcut for columns - because it's reserved for use with rows:
slice_rows = f500_selection["State Grid":"Toyota Motor"]
print(type(slice_rows))
print(slice_rows)

#outout
class 'pandas.core.frame.DataFrame'

                          rank  revenues  profits country
State Grid                   2    315199   9571.3   China
Sinopec Group                3    267518   1257.9   China
China National Petroleum     4    262573   1867.5   China
Toyota Motor                 5    254694  16899.3   Japan
  
  
# example
toyota = f500.loc["Toyota Motor"]

drink_companies = f500.loc[["Anheuser-Busch InBev", "Coca-Cola", "Heineken Holding"]]

middle_companies = f500.loc["Tata Motors":"Nationwide", "rank":"country"]

# count method with series, it doesn't work on dataframe - Series.value_counts()

sectors = f500["sector"] # it's a serie

sectors_value_counts = sectors.value_counts()
print(sectors_value_counts)

#output
Financials                       118
Energy                            80
Technology                        44
Motor Vehicles & Parts            34
Wholesalers                       28
Health Care                       27
Food & Drug Stores                20
Transportation                    19
Telecommunications                18
Retailing                         17
Materials                         16
Food, Beverages & Tobacco         16
Industrials                       15
Aerospace & Defense               14
Engineering & Construction        13
Chemicals                          7
Hotels, Restaurants & Leisure      3
Media                              3
Business Services                  3
Household Products                 3
Apparel                            2
Name: sector, dtype: int64
# dataframe method doesnt work

#As with dataframes, we can use Series.loc[] to select items from a series using single labels, a list, or a slice object. 
#We can also omit loc[] and use bracket shortcuts for all three:

Select by Label	           Explicit Syntax	                   Shorthand Convention
Single item from series	   s.loc["item8"]	                    s["item8"]
List of items from series	 s.loc[["item1","item7"]]	          s[["item1","item7"]]
Slice of items from series	s.loc["item2":"item4"]	            s["item2":"item4"]

# resume to label selection

Select by Label	                             Explicit Syntax	                               Shorthand Convention
Single column from dataframe	                df.loc[:,"col1"]	                              df["col1"]
List of columns from dataframe	              df.loc[:,["col1","col7"]]	                     df[["col1","col7"]]
Slice of columns from dataframe	             df.loc[:,"col1":"col4"]	
Single row from dataframe	                   df.loc["row4"]	
List of rows from dataframe	                 df.loc[["row1", "row8"]]	
Slice of rows from dataframe	                df.loc["row3":"row5"]	                         df["row3":"row5"]
Single item from series	                     s.loc["item8"]	                                s["item8"]
List of items from series	                   s.loc[["item1","item7"]]	                      s[["item1","item7"]]
Slice of items from series	                  s.loc["item2":"item4"]	                        s["item2":"item4"]

# exercice
big_movers = f500.loc[["Aviva", "HP", "JD.com", "BHP Billiton"],["rank","previous_rank"]]

bottom_companies = f500.loc["National Grid" : "AutoNation", ["rank", "sector", "country"]]

print(big_movers)

#output
rank  previous_rank
Aviva           90            279
HP             194             48
JD.com         261            366
BHP Billiton   350            168



print(bottom_companies)
#output
                                       rank              sector  country
National Grid                           491              Energy  Britain
Dollar General                          492           Retailing      USA
Telecom Italia                          493  Telecommunications    Italy
Xiamen ITG Holding Group                494         Wholesalers    China
Xinjiang Guanghui Industry Investment   495         Wholesalers    China
Teva Pharmaceutical Industries          496         Health Care   Israel
New China Life Insurance                497          Financials    China
Wm. Morrison Supermarkets               498  Food & Drug Stores  Britain
TUI                                     499   Business Services  Germany
AutoNation                              500           Retailing      USA
  
# Subtract the values in the rank column from the values in the previous_rank column. Assign the result to rank_change.
rank_change = f500["previous_rank"] - f500["rank"] # mudança do rank mundial das empresas


# series methods
Series.max()
Series.min()
Series.mean()
Series.median()
Series.mode()
Series.sum()

# example
rank_change_max = rank_change.max()

rank_change_min = rank_change.min()
#output - teria que ter o print, mas fiquei com preguiça :)
226 # biggest increase in the rank
-500 # biggest decrease in the rank - mas a lista só tem 500 numeros, então mesmo se a empresa fosse a primeira e depois a ultima, seria uma queda de 499

# describe method
assets = f500["assets"]
print(assets.describe())

# output
count    5.000000e+02
mean     2.436323e+05
std      4.851937e+05
min      3.717000e+03
25%      3.658850e+04
50%      7.326150e+04
75%      1.805640e+05
max      3.473238e+06
Name: assets, dtype: float64

Original          Notation	Expanded             Formula	Result
5.000000E+02	     5.000000 * 10 ** 2	           500
2.436323E+05	     2.436323 * 10 ** 5	           243632.3

#If we use describe() on a column that contains non-numeric values, we get some different statistics. Let's look at an example:

country = f500["country"]
print(country.describe())

#output
count     500
unique     34
top       USA
freq      132
Name: country, dtype: object

The first statistic, count, is the same as for numeric columns, showing us the number of non-null values. The other three statistics are new:

unique: Number of unique values in the series. In this case, it tells us that there are 34 different countries represented in the Fortune 500.
top: Most common value in the series. The USA is the country that headquarters the most Fortune 500 companies.
freq: Frequency of the most common value. Exactly 132 companies from the Fortune 500 are headquartered in the USA.

#example 02
rank = f500["rank"]

rank_desc = rank.describe()
print(rank_desc)

#Output
count    500.000000
mean     250.500000
std      144.481833
min        1.000000
25%      125.750000
50%      250.500000
75%      375.250000
max      500.000000
Name: rank, dtype: float64

prev_rank = f500["previous_rank"]
print(prev_rank.describe())

#output
count    500.000000
mean     222.134000
std      146.941961
min        0.000000 # valor meio bizarro, não existe rank 0, e sim de 1-500
25%       92.750000
50%      219.500000
75%      347.250000
max      500.000000
Name: previous_rank, dtype: float64

  
# we can use the counts method in one line  
countries_counts = f500["country"].value_counts() # conta a quantidade de empresas que cada país tem
# loc method the same thing
print(f500["country"].value_counts().loc["China"])
#output
109 # encontrou a china com 109 empresas
  
  
 # example 
 
zero_previous_rank_bool = f500["previous_rank"] == 0 # vai ter um dataframe que essa coluna será falsa ou verdadeira
zero_previous_rank_df = f500[zero_previous_rank_bool] # data frame apenas com os verdadeiros (valores == 0)
zero_previous_rank_series = zero_previous_rank_df["previous_rank"] # series do df

zero_previous_rank = len(zero_previous_rank_series) # len da series

# other option in one line
zero_previous_rank = f500["previous_rank"].value_counts().loc[0] # já procura a quantidade de itens que tem na coluna previous_rank = 0

# we conclude that these companies did"t hava a rank at all for the previous year


Dataframe.method(axis=0) or dataframe.method(axis="index")
calculates along  the row

Dataframe.method(axis=1) or dataframe.method(axis="column")
calculates along  the column


## WITH I WANT TO SEE THE MAX VALUE FOR EACH NUMERIC COLUMN 
max_f500 = f500.max(numeric_only = True)

#output
rank                            500.0
revenues                     485873.0
revenue_change                  442.3
profits                       45687.0
assets                      3473238.0
profit_change                  8909.5
previous_rank                   500.0
years_on_global_500_list         23.0
employees                   2300000.0
total_stockholder_equity     301893.0
dtype: float64


# DESCRIBE ONLY IN THE DATAFRAME THE VALUES COLUMNS
f500_desc = f500.describe()

# DESCRIBE ALL THE VALUES AND THE OBJECTS
print(f500.describe(include=['O']))
_            ceo    industry     sector  country  hq_location    website
count        500         500        500      500          500        500
unique       500          58         21       34          235        500
top     Xavie...   Banks:...  Financ...      USA  Beijing,...  http:/...
freq           1          51        118      132           56          1

#boolean 

top5_rank_revenue["revenues"] = 0
print(top5_rank_revenue)

#output
_                        rank  revenues
Walmart                      1         0
State Grid                   2         0
Sinopec Group                3         0
China National Petroleum     4         0
Toyota Motor                 5         0
  
top5_rank_revenue.loc["Sinopec Group", "revenues"] = 999
print(top5_rank_revenue)

#output
_                         rank  revenues
Walmart                      1         0
State Grid                   2         0
Sinopec Group                3       999
China National Petroleum     4         0
Toyota Motor                 5         0

#The company "Dow Chemical" has named a new CEO. 
#Update the value where the row label is Dow Chemical and for the ceo column to Jim Fitterling in the f500 dataframe.

f500.loc["Dow Chemical", "ceo"] = "Jim Fitterling"

#Create a boolean series, motor_bool, that compares whether the values in the industry column from the f500 dataframe are equal to "Motor Vehicles and Parts".
motor_bool = f500["industry"] == "Motor Vehicles and Parts"
# Use the motor_bool boolean series to index the country column. Assign the result to motor_countries.
motor_countries = f500.loc[motor_bool, "country"]

# This uses Series.value_counts() and Series.head() to display the 5 most common values in the previous_rank column, 
#but adds an additional dropna=False parameter, which stops the Series.value_counts() method from excluding null values when it 
#makes its calculation, as shown in the Series.value_counts() documentation.
import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()

#befor
previous_rank
0	33
159	1
147	1
148	1
#after
previous_rank
NaN	33
471.0	1
234.0	1
125.0	1

# add a new column
top5_rank_revenue["year_founded"] = 0
print(top5_rank_revenue)

#output
_                         rank  revenues  year_founded
Walmart                      1         0             0
State Grid                   2         0             0
Sinopec Group                3       999             0
China National Petroleum     4         0             0
Toyota Motor                 5         0             0

# add a new column - with the diference between 2 columns

f500["rank_change"] = f500["previous_rank"] - f500["rank"]

rank_change_desc = f500["rank_change"].describe()

#print the top2 
#01 challenge
usa_bool = f500["country"] == "USA"
usa_df = f500[usa_bool] # peguei uma serie de valores falsos e inseri no df (tipo um filtro)

usa_series = usa_df["industry"]
industry_usa = usa_series.value_counts().head(2)
print(industry_usa)

# 02 challenge
china_bool = f500["country"] == "China"
china_df = f500[china_bool] # peguei uma serie de valores falsos e inseri no df (tipo um filtro)
china_series = china_df["sector"]
sector_china = china_series.value_counts().head(3)
print(sector_china)

#output

Banks: Commercial and Savings               8
Insurance: Property and Casualty (Stock)    7
Name: industry, dtype: int64
  
Financials     25
Energy         22
Wholesalers     9
Name: sector, dtype: int64
#boa


# Exploring Data with Pandas
import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500.loc[:,["rank", "revenues", "revenue_change"]].head()

#Output
                          rank  revenues  revenue_change
Walmart                      1    485873             0.8
State Grid                   2    315199            -4.4
Sinopec Group                3    267518            -9.1
China National Petroleum     4    262573           -12.3
Toyota Motor                 5    254694             7.7




















  
  
  


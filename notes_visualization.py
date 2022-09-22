#Numpy

# Below is information about selected columns from the dataset:

#pickup_year: the year of the trip
#pickup_month: the month of the trip (January is 1, December is 12)
#pickup_day: the day of the month of the trip
#pickup_location_code: the airport or borough where the the trip started
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


# challenge nparray

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


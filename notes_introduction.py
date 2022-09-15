# sum of elements using for loop - exemple 01
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]
##
app_data_set = [row_1, row_2, row_3, row_4, row_5] # list of a list 

rating_sum = 0

for row in app_data_set:
    rating_sum = rating_sum + row[-2]
    print(rating_sum)

# average in a simple list
data = [4, 5, 10, 12, 15, 17]
sum_data = 0

for numbers in data:
    sum_data = numbers + sum_data
avg_data = sum_data/len(data)
print(avg_data)

# avg in a list of a list exemple 01
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

rating_sum = 0

for row in app_data_set:
    rating = row[-1]
    rating_sum = rating_sum + rating 
avg_rating = rating_sum/len(app_data_set)
print(avg_rating)

# open a csv file and transform it in a list of a list

opened_file = open('AppleStore.csv')

from csv import reader

read_file = reader(opened_file)
apps_data = list(read_file)
print(len(apps_data))
print(apps_data[0]) # only print the first row
print(apps_data[1:3]) # print the second and third row

## use this csv file and try to interate over the data, after that take the avg from the rating values
from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = 0
for row in apps_data[1:] : # "deleted" the first row, witch is the head from the dataset
    rating = float(row[7]) # extract the rating value from each row 
    rating_sum = rating_sum + rating
avg_rating = rating_sum/len(apps_data[1:]) # this will count only the data, not the head 
print(avg_rating)
 

# Append functions
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

rating_sum = [] # Step 1
for row in app_data_set:
    rating = row[-1] # Step 2
    rating_sum.append(rating) # Step 3

print(rating_sum)

avg_rating = sum(rating_sum) / len(rating_sum) # Step 4
print(avg_rating)

# Append function with csv file 
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = []
for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum.append(rating) # we don't need to create a variable ("rating_sum) in this case 
    
avg_rating = sum(rating_sum)/len(rating_sum)
print(avg_rating)

# using the same method but to retreave the names
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_names = []
for row in apps_data[1:]:
    name = row[1] # second element in each row
    apps_names.append(name)
print(apps_names[:5]) # first five elements


# if statement (for free apps on applestore)
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price == 0 :
        free_apps_ratings.append(rating)
avg_rating_free = sum(free_apps_ratings)/len(free_apps_ratings)


                     

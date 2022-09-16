# FOR LOOP

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

# -----------------------------------------------------------------------

# IF/ELSE/ELIF STATEMENT 

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

# If statement easly to understand
app_and_price = [['Facebook', 0], ['Instagram', 0], ['Plants vs. Zombies', 0.99], ['Minecraft: Pocket Edition', 6.99], ['Temple Run', 0], ['Plague Inc.', 0.99]]

free_apps = []
for app in app_and_price:
    name = app[0]
    price = app[1]

    if price == 0:
        free_apps.append(name)

print(free_apps)

# Output
['Facebook', 'Instagram', 'Temple Run']

# if statement non_free_app on the apple_store
# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price != 0.0: # diferent of zero
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)
print(avg_rating_non_free)

# non game app rating by genre - determine the average rating of free gaming apps.

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_games_ratings = []
for row in apps_data[1:] :
    rating = float(row[7])
    genre = row[11]
    if genre != 'Games': # if the genre is not equal to 'Games'
        non_games_ratings.append(rating)
avg_rating_non_games = sum(non_games_ratings)/len(non_games_ratings)
print(avg_rating_non_games)

# usign AND on if statement - avg of free games apps
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    # Complete code from here
    if price == 0.0 and genre == 'Games':
        free_games_ratings.append(rating)
avg_rating_free_games = sum(free_games_ratings)/len(free_games_ratings)
print(avg_rating_free_games)

# if statement OR - avg rating of social app and games combined 
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)
avg_games_social = sum(games_social_ratings)/len(games_social_ratings)
print(avg_games_social)

# working with more than 1 and/or 

# We want this logic:
if (genre == 'Social Networking' or genre == 'Games') and price ==0;

# Not this logic:
if genre == 'Social Networking' or (genre == 'Games' and price ==0);

print((True or False) and False)
#output
False

# between values
x = -6
y = 14
z = 8.5

if x > z:
    print('x is greater than z')
if y != z:
    print('y is not equal to z')
if z >= x and z <= y:
    print('z is between x and y')
    
# How many apps have a rating of 4.0 or greater? ( in 2 ways)

apps_4_or_greater = []

for row in apps_data[1:]:
    rating = float(row[7])
    if rating >= 4.0:
        apps_4_or_greater.append(rating)

print(len(apps_4_or_greater))

# second option

n_of_apps = 0

for row in apps_data[1:]:
    rating = float(row[7])
    if rating >= 4.0:
        n_of_apps = n_of_apps + 1

print(n_of_apps)

# same output = 4781

# What is the average rating of the apps that have a price greater than $9?
#How many apps have a price greater than $9?
#How many apps have a price less than or equal to $9?        


 
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    
    if price > 9:
        ratings.append(rating)
        
avg_rating = sum(ratings) / len(ratings)
n_apps_more_9 = len(ratings)
n_apps_less_9 = len(apps_data[1:]) - len(ratings)

print(avg_rating)
print(n_apps_less_9)
print(n_apps_more_9)

# else statement

apps_data = [['Call of Duty: Zombies', 5.0], ['Facebook', 0.0], ['Instagram', 0.0], ['Temple Run', 0.0]]

for app in apps_data:
    price = app[1]

    if price == 0.0:
        app.append('free')
    else:
        app.append('not free')

print(apps_data)

#output
[['Call of Duty: Zombies', 5.0, 'not free'], ['Facebook', 0.0, 'free'], ['Instagram', 0.0, 'free'], ['Temple Run', 0.0, 'free']]

# other exemple
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append('free')
    else:
        app.append('not free')
apps_data[0].append('free_or_not')   # just create a new column to represent the free or not free strings     
print(apps_data[:6])

# elif statement

# to avoid redundance in our code
apps_data = [['Facebook', 0.0], ['Notion', 14.99], ['Astropad Standard', 29.99], ['NAVIGON Europe', 74.99]]

for app in apps_data:
    price = app[1]

    if price == 0.0:
        app.append('free')
    if price > 0.0 and price < 20:
        app.append('affordable')
    if price >= 20 and price < 50:
        app.append('expensive')
    if price >= 50:
        app.append('very expensive')

print(apps_data)

# the code below it's a redundance 
app_ratings = [['Facebook', 3.5], ['Notion', 4.0], ['Astropad Standard', 4.5], ['NAVIGON Europe', 3.5]]

for app in app_ratings: # ele tá pegando a lista dentro da lista
    rating = app[1] # he is retrieve the second element in the list
    if rating < 3.0:
        app.append('below average') # está adicionando essa string dentro da lista
    elif rating >= 3.0 and rating < 4.0:
        app.append('roughly average')
    else:
        app.append('better than average')
print(app_ratings)

# output
[['Facebook', 3.5, 'roughly average'], ['Notion', 4.0, 'better than average'], ['Astropad Standard', 4.5, 'better than average'], ['NAVIGON Europe', 3.5, 'roughly average']]

# elif statement in the file from apple store

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append('free')
    elif price > 0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    elif price >= 50:
        app.append('very expensive')
apps_data[0].append('price_label')
print(apps_data[:6])
#output
[['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic', 'price_label'], 
 ['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1', 'free'], 
 ['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1', 'free'], 
 ['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1', 'free'], 
 ['420009108', 'Temple Run', '65921024', 'USD', '0.0', '1724546', '3842', '4.5', '4.0', '1.6.2', '9+', 'Games', '40', '5', '1', '1', 'free'], 
 ['284035177', 'Pandora - Music & Radio', '130242560', 'USD', '0.0', '1126879', '3594', '4.0', '4.5', '8.4.1', '12+', 'Music', '37', '4', '1', '1', 'free']]

# change the date
date = "July 23, 2009"
year = fetch_year("July 23, 2009")
print(year)

#output
2009

# -------------------------------------------------------------
# DICTIONARIES

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings

result = 'It exists'
if '17+' in content_ratings:
    print(result)

# To use code to count how many times each rating occurs in this short list, let's complete the following:
content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}
ratings = ['4+', '4+', '4+', '9+', '9+', '12+', '17+']

for c_rating in ratings:
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1

print(content_ratings)

#output
{'4+': 3, '9+': 2, '12+': 1, '17+': 1}


# Add values in the keys from the file

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}

for row in apps_data[1:]:
    c_rating = row[10] 
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
print(content_ratings)

#output
{'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
        
# more effictive method

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}
for row in apps_data[1:]:
    c_rating = row[10] 
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
        
print(content_ratings)

#output
{'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}

# same idea

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}
for row in apps_data[1:]:
    genre = row[11]
    if genre in genre_counting:
        genre_counting[genre] += 1 
    else:
        genre_counting[genre] = 1 # coloca genre como key e 1 como value
print(genre_counting) 

# output
{'Social Networking': 167, 'Photo & Video': 349, 'Games': 3862, 'Music': 138, 'Reference': 64, 'Health & Fitness': 180, 'Weather': 72, 
 'Utilities': 248, 'Travel': 81, 'Shopping': 122, 'News': 75, 'Navigation': 46, 'Lifestyle': 144, 'Entertainment': 535, 'Food & Drink': 63, 
 'Sports': 114, 'Book': 112, 'Finance': 104, 'Education': 453, 'Productivity': 178, 'Business': 57, 'Catalogs': 10, 'Medical': 23}


# devided - proportion 
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for iteration_variable in content_ratings: # interation_variable são as keys
    content_ratings[iteration_variable] /= total_number_of_apps

print(content_ratings)

# other exemple

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for rating in content_ratings: # rating is the key
    content_ratings[rating] /= total_number_of_apps #Transform the dictionary value (the frequency) to a proportion by dividing it by the total number of apps.
    content_ratings[rating] *= 100 # Transform the updated dictionary value (the proportion) to a percentage by multiplying it by 100.

print(content_ratings)
# output
{'4+': 61.595109073224954, '12+': 16.04835348061692, '9+': 13.714047519799916, '17+': 8.642489926358204}

percentage_17_plus = content_ratings['17+'] # Determine the percentage of apps that have a content rating of '17+' and assign your answer to a variable named percentage_17_plus.
percentage_15_allowed = content_ratings['4+'] + content_ratings['9+'] + content_ratings['12+'] # Determine the percentage of apps that a 15-year-old can download and assign your answer to a variable named percentage_15_allowed

# When we transform frequencies to proportions, we can create a new dictionary instead of overwriting the values in the initial dictionary. 
#To do that, we can create a new empty dictionary and populate it within the loop:

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
c_ratings_proportions = {}

for key in content_ratings:
    proportion = (content_ratings[key] / total_number_of_apps)     
    c_ratings_proportions[key] = proportion

print(c_ratings_proportions)
print(content_ratings)

#output
{'4+': 0.6159510907322495, '12+': 0.16048353480616923, 
 '9+': 0.13714047519799916, '17+': 0.08642489926358204}
{'4+': 4433, '12+': 1155, '9+': 987, '17+': 622} # so, e don't need to change the original dictionary, like the other exercice

# percentage and proportion

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

for key in content_ratings:
    proportion = (content_ratings[key] / total_number_of_apps)     
    c_ratings_proportions[key] = proportion # save in the dictionary the value "proportion"
    percentage = (content_ratings[key] / total_number_of_apps) * 100
    c_ratings_percentages[key] = percentage
print(c_ratings_proportions)
print(c_ratings_percentages)

#output
{'4+': 0.6159510907322495, '12+': 0.16048353480616923, '9+': 0.13714047519799916, '17+': 0.08642489926358204}
{'4+': 61.595109073224954, '12+': 16.04835348061692, '9+': 13.714047519799916, '17+': 8.642489926358204}

# min and max LIST
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = []
for row in apps_data[1:]:
    size = float(row[2]) # quer dizer que nesta row queremos pegar o index 2 (terceiro elemento)
    data_sizes.append(size)
min_size = min(data_sizes)
max_size = max(data_sizes)

# full exemple

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

n_user_ratings = []
for row in apps_data[1:]:
    n_user_ratings.append(int(row[5]))
    
ratings_max = max(n_user_ratings)
ratings_min = min(n_user_ratings)

user_ratings_freq = {'0 - 10000': 0, '10000 - 100000': 0, '100000 - 500000': 0,
                    '500000 - 1000000': 0, '1000000+': 0}

for row in apps_data[1:]:
    user_ratings = int(row[5])
    
    if user_ratings <= 10000:
        user_ratings_freq['0 - 10000'] += 1
        
    elif 10000 < user_ratings <= 100000:
        user_ratings_freq['10000 - 100000'] += 1
        
    elif 100000 < user_ratings <= 500000:
        user_ratings_freq['100000 - 500000'] += 1
        
    elif 500000 < user_ratings <= 1000000:
        user_ratings_freq['500000 - 1000000'] += 1
        
    elif user_ratings > 1000000:
        user_ratings_freq['1000000+'] += 1


print(user_ratings_freq)

# output
{'0 - 10000': 6181, '10000 - 100000': 798, '100000 - 500000': 196, '500000 - 1000000': 16, '1000000+': 6}



#----------------------------------------------------------

# FUNCTIONS

# try to understant the function len() with a for loop

list_1 = [21, 0, 72, 2, 5]

length = 0
for element in list_1:
    length += 1

print(length)

# output
5

# try to understand the sum()

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]
sum_manual = 0
for number in a_list:
    sum_manual = number + sum_manual
print(sum_manual)
print(sum(a_list))

# output
103945
103945

# frequency in a list

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}
for value in ratings:
    if value in content_ratings:
        content_ratings[value] += 1
    else:
        content_ratings[value] = 1
print(content_ratings)

# output
{'4+': 3, '9+': 1, '12+': 2, '17+': 2}

# create a function
def square(a_number):
    squared_number = a_number * a_number
    return squared_number
squared_10 = square(10)
squared_16 = square(16)

# create a function 2 - function tht add 10 

def add_10(a_number):
    added_number = a_number + 10
    return added_number
add_30 = add_10(30)
add_90 = add_10(90)

#output
40
100

a_number = 'parameter'
30 = 'argument' # for exemple

# other function
def date(year, month, day):
    return month + " " + str(day) + ', ' + str(year)

print(date(2006, 'July', 15))
print(date(2004, 'February', 4))
print(date(1949, 'June', 9))

#output
July 15, 2006
February 4, 2004
June 9, 1949


# Function to extract a column

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
# Write a function named extract() that can extract any column you want from the apps_data dataset.
def extract(index_number):
    content_list = []
    for row in apps_data[1:]:
        col_values = row[index_number]
        content_list.append(col_values)
    return content_list
genres = extract(11)

print(genres)


#output 
# ['Social Networking', 'Photo & Video', 'Games', 'Games', 'Music', 'Social Networking', 'Reference', 'Games', 'Music', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Health & Fitness', 'Games', 'Weather', 'Games', 'Utilities', 'Games', 'Games', 'Travel', 'Games', 'Games', 'Shopping', 'Games', 
#'Games', 'Games', 'Games', 'Music', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Health & Fitness', 'Social .......]
 
 # nice example to take frequency in any list 
 # CODE FROM THE PREVIOUS SCREEN
 
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
 
# extract function
def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)
     return column

genres = extract(11)
# frequency function
def freq_table(a_list):
    dict_freq = {}
    for value in a_list:
        if value in dict_freq: 
            dict_freq[value] += 1 # if the value is in the dict, add 1
        else:
                dict_freq[value] = 1
    return dict_freq

genres_ft = freq_table(genres)

print(genres_ft)
 
#output
 {'Social Networking': 167, 'Photo & Video': 349, 'Games': 3862, 'Music': 138, 'Reference': 64, 'Health & Fitness': 180, 'Weather': 72, 
  'Utilities': 248, 'Travel': 81, 'Shopping': 122, 'News': 75, 'Navigation': 46, 'Lifestyle': 144, 'Entertainment': 535, 'Food & Drink': 63, 
  'Sports': 114, 'Book': 112, 'Finance': 104, 'Education': 453, 'Productivity': 178, 'Business': 57, 'Catalogs': 10, 'Medical': 23}
 
# function frequency and extract the column
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(index):
    dict_freq = {}
    for row in apps_data[1:]:
        value = row[index]
        if value in dict_freq:
            dict_freq[value] += 1
        else:
            dict_freq[value] = 1
    return dict_freq
ratings_ft = freq_table(7)
print(ratings_ft)

#output
{'3.5': 702, '4.5': 2663, '4.0': 1626, '3.0': 383, '5.0': 492, '2.5': 196, '2.0': 106, '1.5': 56, '1.0': 44, '0.0': 929}

# MULTIPLE FUNCTION (EXTRACT THE COLUMN, DO THE FREQUENCY AND TAKE THE DATASET)

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(index, dataset):
    frequency_table = {}
    
    for row in dataset[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table
ratings_ft = freq_table(7, apps_data)

print(ratings_ft)
#output
{'3.5': 702, '4.5': 2663, '4.0': 1626, '3.0': 383, '5.0': 492, '2.5': 196, '2.0': 106, '1.5': 56, '1.0': 44, '0.0': 929}


# AVERAGE FOR EVERY INDEX IN EVERY DATASET (IMPORTANT)
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    extract_list = extract(data_set = data_set, index = index)
    sum_list = find_sum(a_list = extract_list)
    len_list = find_length(a_list = extract_list)
    mean_list = sum_list/len_list
    # it will be the same way - if> mean_list = find_sum(extract_list)/find_lenght(extract_list)
    
    return mean_list
avg_price = mean(apps_data, 4)
print(avg_price)

#OUTPUT
1.7262178685562666


#---------------------------------------------

# Buil-in functions
# fixar uma "constante" na funcao, para acelerar o processo de code

def open_dataset(file_name = 'AppleStore.csv'):
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data
apps_data = open_dataset()

 
# other functions (multiple funcions)

def sum_or_difference(a, b, return_sum=True):
    if return_sum:
        return a + b
    else:
        return a - b

print(sum_or_difference(10, 5, return_sum=True))
print(sum_or_difference(10, 5, return_sum=False))
# output
15
5

# take or not the header from a file csv
def open_dataset(file_name='AppleStore.csv', header = True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    if header:
        return data[1:]
    else:
        return data
apps_data = open_dataset(file_name = 'AppleStore.csv', header = True)
# or we can do like:
apps_data = open_dataset()

# function wich shows us multiples response

def pythagorean(a, b):
    a_squared = a**2
    b_squared = b**2
    c_squared = a_squared + b_squared
    return a_squared, b_squared, c_squared
print(pythagorean(5,12))
# output
(25, 144, 169) # tuple

# diference between list and tuples
#The main difference between tuples and lists is whether we can modify the existing values or not. In the case of tuples, we can't 
#modify the existing values, while in the case of lists, we can. Below, we're trying to modify the first value of a list and a tuple.
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0] # the data first, and than the header
    else:
        return data
all_data = open_dataset()
header = all_data[-1] # just the header
apps_data = all_data[0] # all the data

print(header)

# print individual data for each (header, apps_data)
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data

apps_data, header = open_dataset() # a tuple can be "divided by element - list can be the same thing
print(header)
#output
['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 
 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']

# function without return, will act imedeatly - see the exemple below
def price(item, cost):
    print("The " + item + " costs $" + str(cost) + ".")

price("chair", 40.99) # don't need to write print
price("book", 12.84)
price("soap", 3.95)
#output
The chair costs $40.99.
The book costs $12.84.
The soap costs $3.95.

# global scope
e = 'mathematical constant'
a_sum = 1000
length = 50

def exponential(x):
    e = 2.72**x
    return e**x
result = exponential(5)
print(result) 
print(e)

def divide():
    print(a_sum)
    print(length)
    return a_sum/length
result_2 = divide() # no error 

# When a variable is accessed from within a function, Python first searches in the local scope (inside that function's definition) to see if the variable
#is defined there. If it doesn't find it there, it doesn't cause an error; rather, it continues to search in the global scope (the scope of the main 
#program).


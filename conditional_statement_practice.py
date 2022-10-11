# If we run this Python code, what will be printed to the screen?

x = 3
y = 2
z = 1
if x > y:
    print('A')
if y > z:
    print('B')
if z > x:
    print('C')
#Output
A
B

-------------------
#If we run this Python code, what will be printed to the screen?

x = 3
y = 2
z = 1
if x > y:
    print('A')
elif y > z:
    print('B')
elif z > x:
    print('C')
# como o primeiro já é verdadeiro, o programa não precisa rodar os outros
#Output
A

------------------
#If we run this Python code, what will be printed to the screen?
# Write your answer below
if True:
    print('A')
elif True:
    print('B')
    
#Output
A

-------------------
# If we run this Python code, what will be printed to the screen?
if True and True:
    print('A')
if True and False:
    print('B')
if False and True:
    print('C')
if False and False:
    print('D')
#Output
A

-------------------
#If we run this Python code, what will be printed to the screen?
if True or True:
    print('A')
if True or False:
    print('B')
if False or True:
    print('C')
if False or False:
    print('D')
# apenas D não será output

-------------------
#If we run this Python code, what will be printed to the screen?
if False or True and False:
    print('A')
if True or False and False:
    print('B')
# apeas a B terá output (começamos pelo AND primeiro para calcular)

-------------------
# Given a list of integers, write a Python program that counts how many values in the list are greater than 100

#Write a program to count how many numbers greater than 100 are in the values list.
#Assign the answer to a variable named num_bigger.

values = [80, 109, 111, 109, 94, 93, 108, 107, 81, 111, 114, 102, 81, 107, 120, 108, 92, 113, 119, 97]

num_bigger = 0
for value in values:
    if value > 100:
        num_bigger += 1
print(num_bigger)

#output
13

-------------------
# Given a list of integers, write a Python program that counts how many even and odd values it contains.

values = [80, 109, 111, 109, 94, 93, 108, 107, 81, 111, 114, 102, 81, 107, 120, 108, 92, 113, 119, 97]

num_even = 0
num_odd = 0
for value in values:
    if value%2 == 0:
        num_even += 1
    else:
        num_odd += 1
print(num_even)
print(num_odd)

#Output
8
12

-------------------
# Write a Python program that checks whether two given lists are the reverse of one another.
values1 = [80, 109, 111, 109, 94, 93, 108, 107, 81, 111, 101, 114, 102, 81, 107, 120, 108, 92, 113, 119, 97]
values2 = [97, 119, 113, 92, 108, 120, 107, 81, 102, 114, 110, 111, 81, 107, 108, 93, 94, 109, 111, 109, 80]

# Write your answer below
reversed_values = []
for i in range(len(values1)):
    reversed_values.append(values1[-i -1])

is_reversed = 0
if reversed_values == values2:
    is_reverse = True
else:
    is_reverse = False


-------------------
# reverse exemple

values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 17, 14, 1, 9]

# Write your answer below
reversed_values = []
for i in range(len(values)):
    reversed_values.append(values[-i -1])

 -------------------   
# Write a program that creates a list named common that contains the characters that are common to both s1 and s2.

s1 = 'I have been busier these days due to having a lot on my plate.'
s2 = 'You have been very supportive towards my recent endeavors.'

common = []
for i in s1:
    if i in s2 and i not in common:
        common.append(i)
print(common)

#Output
[' ', 'h', 'a', 'v', 'e', 'b', 'n', 'u', 's', 'i', 'r', 't', 'd', 'y', 'o', 'm', 'p', '.']

 ------------------- 
#Given a list of numbers, calculate the maximum value in that list. The goal is to avoid using the max() function.
values = [72, 48, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 10, 62, 48, 32, 96, 75, 15]

maximum = 0
for value in values:
    if value > maximum:
        maximum = value
print(maximum)
#output
96

 ------------------- 
#Given a list of numbers, calculate the minimum value in that list. The goal is to avoid using the min() function.

values = [72, 48, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 10, 62, 48, 32, 96, 75, 15]

minimum = 10000000 # colocar um numero bem maior para saber que algum da lsita values será menor que minimum
for value in values:
    if value < minimum:
        minimum = value
print(minimum)

#output
6

-------------------
# Given a list of numbers, find a pair of distinct values whose sum is equal to 100.
values = [72, 50, 48, 50, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 10, 62, 48, 32, 96, 75, 15, 50, 50]

value1 = None
value2 = None

for x in values:
    for y in values:
        if x+y == 100 and x != y:
            value1 = x
            value2 = y

------------------
# Given a list of numbers, find the number that appears the most.
values = [72, 50, 48, 50, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 32, 10, 62, 48, 32, 96, 75, 15]

most_frequent = values[0]

for value in values:
    if values.count(value) > values.count(most_frequent):
        most_frequent = value
print(most_frequent)

#output
32
-------------------
#Count how many names have an estimated number greater than or equal to 100,000.
import csv 
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_rows = list(reader)
rows = all_rows[1:]

names_100k =[]
for row in rows:
    value = row[1]
    if float(value) > 100000:
        names_100k.append(row[0])
        
count = len(names_100k)
            
#other option
import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
rows = list(reader)

count = 0
for row in rows[1:]:
    if float(row[1]) >= 100000:
        count += 1

print(count)

#output
6

-------------------
# In this problem, you'll create a new list containing only the rows where the length of the corresponding name is greater than 10
import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_rows = list(reader)
rows = all_rows[1:]

longest_names = []
for row in rows:
    value = row[0]
    if len(value) > 10:
        longest_names.append(value)

print(longest_names[:5])

-------------------
# In this practice problem, you'll need to find the most common unisex named. This means finding the name for which the estimated_number is the largest.
import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_rows = list(reader)
rows = all_rows[1:]

maximum = None
max_name = None
for row in rows:
    if maximum == None or float(row[1]) > maximum:
        maximum = float(row[1])
        max_name = row[0]
print(max_name)
    
#Output
Casey

-------------------
# Let's calculate all names that have an estimated number of at most 1,000 people (inclusive).
import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_rows = list(reader)
rows = all_rows[1:]

rare_names = []
for row in rows:
    value = row[1]
    if float(value) <= 1000:
        rare_names.append(row[0])
        
print(rare_names[:5])

#output
['Eliyah', 'Tonnie', 'Teagen', 'Rudi', 'Kamani']


            
            
            
            
            
            
            
            
            
            
            
            
            































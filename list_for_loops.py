# Print all sentences contained in the lines list, one per line.
lines = ["My candle burns at both ends;", "It will not last the night;", "But ah, my foes, and oh, my friends —", "It gives a lovely light."]

# Write your answer below
for i in lines:
    print(i)
    
--------------- 
# Your task is to print all values from 0 to N (inclusive).
N = 11

# Write your answer below
for i in range(N+1):
    print(i)
    
---------------     
# Your task is to print all numbers from 42 to 59 (inclusive).
for i in range(42,60):
    print(i)

# Increase by one each value contained in the values list.
values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 10, 14, 17, 14, 1, 16, 19, 7, 9, 19]

--------------- 
# Write your answer below
for i in range(len(values)):
    values[i] += 1

for n in values:
    n = n+1
    print(n)
    
---------------     
# Define a reversed_values variable whose values are the values in the values list, but in reversed order.
values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 17, 14, 1, 9]

# Write your answer below
reversed_values = []
for i in range(len(values)):
    reversed_values.append(values[-i -1])

--------------- 
# What will be the value of values_copy after we execute the following code:
values = [5, 4, 7, 8, 9, 3]

values_copy = []
for v in values:
    values_copy = v
answer = values_copy 
# values_copy vai ser 3, pq ele vai pegar apenas o numero que dará no final da lista

--------------
# What will be the values of x and total after we execute the following code:
values = [3, 5, 2, 1]

total = 0
for x in values:
    total += x
    
answer_x = x
answer_total = total 
# valor de x vai ser o ultimo numero da lista, e o valor do total será a soma total 

--------------- 
# What will be the value of x after we execute the following code:
values = [3, 5, 2, 1]

for x in values:
    x = 0
answer = x
# x vai ser 0

--------------- 
# What will be the values of x and total after we execute the following code:
values = [3, 5, 2, 1]

total = 0
for x in values:
    total = x
answer_x = x
answer_total = total
# x e total vai ser igual a 1

--------------- 
# How many values will be printed if we execute the following code:
for i in range(10):
    print(i)
    i = 11
# 10 valores - de 0 à 9, pq i=11 não vai ser printado  

--------------- 
# What will be the value of values_copy after we execute the following code:
values = [5, 4, 7, 8, 9, 3]

values_copy = []
for v in values:
    values_copy.append(v)
# vai dar a lista copiada, pq voce tá add um numero dentro dessa lis values = values_copy

--------------- 
# Write a Python program that creates a list of lists named matrix_of_ones that represents a 7 by 3 matrix where each number is equal to 1.
matrix_of_ones = []
for _ in range(7):
    matrix_of_ones.append([1, 1, 1])
    
"""
In the for loop we used _ instead 
of a variable name. This can be done when
we don't use the iteration variable.
"""
print(matrix_of_ones)

#output
[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

--------------- 
# 1. Write a Python program that calculates the number of rows and columns of the matrix stored in variable matrix.
# 2. Assign the number of rows to a variable named num_rows and the number of columns to a variable named num_cols.

matrix = [
    [0, 9, 5, 4, 5, 3, 1, 5, 7],
    [8, 2, 1, 7, 3, 1, 5, 7, 0],
    [1, 5, 3, 2, 7, 1, 4, 4, 8],
    [2, 5, 6, 2, 0, 4, 1, 9, 3],
    [7, 4, 2, 9, 7, 0, 7, 4, 4],
]

# Write your code below
for i in matrix:
    num_cols = len(i)
    num_rows = len(matrix)
print(num_cols)
print(num_rows)

--------------- 
# Write a Python program that sums all values in the matrix stored in variable matrix. Assign the result to a variable named total.
matrix = [
    [0, 9, 5, 4],
    [8, 2, 3, 0],
    [1, 5, 3, 2]
]

# Write your code below
num_rows = len(matrix)
num_cols = len(matrix[0])

total = 0
for row in range(num_rows):
    for col in range(num_cols):
        total += matrix[row][col]

---------------         
# Write a Python program that calculates the average of the values list. Assign the result to a variable named average.
values = [61, 20, 45, 63, 96, 71, 6, 8, 72, 22, 97, 7, 46, 11, 15, 74, 81, 69, 70, 26]

# Write your code below
average = sum(values)/len(values)

#other option 
total = 0
for value in values:
    total += value
average = total/len(values)

---------------  
# Create a list named word_len whose elements are the lengths of the words in words. The first element should be the length of the first word; the second element is the length of the second word, and so on.
words = ['tissue', 'psychology', 'blind', 'assessment', 'dynamic', 'hero', 'circulation', 'merchant', 'publication', 'interference', 'show', 'joy', 'sour', 'aloof', 'grass', 'distortion', 'exclude', 'pressure', 'bullet', 'calf']

# Write your code below
word_len = []

for word in words:
    word_len.append(len(word))
print(word_len)

#Output
[6, 10, 5, 10, 7, 4, 11, 8, 11, 12, 4, 3, 4, 5, 5, 10, 7, 8, 6, 4]

---------------
# Print all characters of sentence, one character per line.
sentence = 'I\'m practicing printing string characters!'

# Write your code below
for i in sentence:
    print(i)

---------------
# open a file and analyze it
from csv import reader

# open a file in a list 
opened_file = open('dq_unisex_names.csv')
read_file = reader(opened_file)
uni_names = list(read_file)
headers = uni_names[0]
rows = uni_names[1:] # tirando a headers
print(headers)


# print the first 5 rows
for i in range(5):
    print(rows[i])
    
--------------

# In this practice problem, you'll read the data from the CSV into a list of lists, and you'll modify the inner lists to include a third value. 
#This value will be the length of the name.
import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_rows = list(reader)
rows = all_rows[1:]
for row in rows:
    name = row[0]
    row.append(len(name))
    
# Testing answer

for i in range(5):
    print(rows[i])
# output
Output
['Casey', '176544.328149', 5]
['Riley', '154860.66517300002', 5]
['Jessie', '136381.830656', 6]
['Jackie', '132928.78874000002', 6]
['Avery', '121797.41951600001', 5]

---------------
import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_rows = list(reader)
rows = all_rows[1:]

for row in rows:
    value = row[1]
    row.append(float(value))
    del row[1]
print(rows[:5])

# output
[['Casey', 176544.328149], ['Riley', 154860.66517300002], ['Jessie', 136381.830656], ['Jackie', 132928.78874000002], ['Avery', 121797.41951600001]]

# SAME RESULT
import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_rows = list(reader)
rows = all_rows[1:]
for row in rows:
    row[1] = float(row[1])
    
# Testing answer
for i in range(5):
    print(rows[i])
print(type(rows[0][1]))

# Output
['Casey', 176544.328149]
['Riley', 154860.66517300002]
['Jessie', 136381.830656]
['Jackie', 132928.78874000002]
['Avery', 121797.41951600001]
<class 'float'>

    
    
    
    
    


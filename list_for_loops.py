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





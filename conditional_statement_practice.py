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































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
    

































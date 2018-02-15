#Christo Dragnev
#2/15/18
#gauss.py
""" - adding numbers between 1,100
total = 0
for i in range(1,101):
    total+=i
print(total)
"""

""" - inputing numbers 
num1 = int(input('Enter a number instead of 1: '))
num2 = int(input('Enter a number instead of 100: '))

total = 0
for i in range(num1, num2+1):
    total+=i
print(total)
"""

num1 = int(input('Enter a number instead of 1: '))
num2 = int(input('Enter a number instead of 100: '))
difference = input('Enter a differnce between each term of the series: ')


total = 0
for i in range(num1, num2+1,difference):
    total = (total + i)+(num2-num1)
print(total)


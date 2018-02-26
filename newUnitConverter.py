#Christo Dragnev
#2/26/18
#newUnitConverter

#Christo Dragnev
#1/29/18
#unitConverter.py

print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celsius to Fahrenheit')
print('5) Quit')

while True:
    num = float(input('Choose a number: '))
    if num == 1:
        mile = float(input('Enter Kilometers to Miles: '))
        print(mile, 'kilometers is', mile*0.621, 'in miles')
    elif num == 2:
        pound = float(input('Enter Kilograms to Pounds: '))
        print(pound, 'Kilograms is', pound*0.45, 'in Pounds')
    elif num == 3:
        gallon = float(input('Enter Liters to Gallons: '))
        print(gallon, 'Liters is', gallon/3.78, 'in Gallons')
    elif num == 4:
        fahrenheit = float(input('Enter Celsius to Fahrenheit: '))
        print(fahrenheit, 'degrees Celsius is', (fahrenheit*(9/5))+32, 'in Fahrenheit')
    elif num == 5:
        break
    else:
        print('Invalid number. Enter number between 1-4')
        

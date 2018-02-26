#Christo Dragnev
#2/26/18
#numberGuessingGame.py

from random import randint

num = randint(1,101)

for i in range(1,13):
    guess = float(input('Guess a number between 1 and 100: '))
    if  guess>num:
        print('too high')
    elif guess<num:
        print('too low')
    else:
        print('You got it in', i ,'tries')

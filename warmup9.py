#Christo Dragnev
#3/1/18
#warmup9.py

text = input('Enter text: ')

for ch in text:
    if ch in 'aeiouAEIOU':
        print(ch.upper())
    else:
        print(ch.lower())

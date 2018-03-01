#Christo Dragnev
#3/1/18
#warmup9.py

text = input('Enter text: ')

for ch in text:
    if 'a' in ch or 'e' in ch or 'i' in ch or 'o' in ch or 'u' in ch or 'y' in ch:
        print(ch.upper())
    else:
        print(ch.lower())

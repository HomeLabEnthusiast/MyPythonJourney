# input()-funktionen är en inbyggd funktion i Python som gör att du kan ta emot indata från användaren.

# 1. Du kan spara värdet i minnet i form av en variabel, såsom name
    # input('What is your name? ') ->
    # name = input('What is your name? ')

# 2. Du kan kombinera 2 olika strings med varandra, inklusive en variabel
    # print('Hi' + name)

# 3. F-strängar med hjälp av {}är ett annat sätt för att kombinera 2 olika strings med varandra
    # f'{name}

name = input('What is your name? ')
print('Hi ' + name)
print('Hi ' f'{name}')


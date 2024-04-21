
# EXERCISE
# Ask two questions: 1. Person's name 2. Favorite color
# Then, print a message like "Tomas likes blue"

name = input('Vad är ditt namn? ')  # Använd input() för att ta emot indata
favorite_color = input('Vad är din favoritfärg? ')  # Använd input() för att ta emot indata
print(f'{name} gillar {favorite_color}')  # Använd f-sträng med {} för att kombinera strings


# Hur koden fungerar nu:

# Koden frågar användaren efter namn och favoritfärg med input().
# Användarens svar lagras i variablerna name och favorite_color.
# Slutligen skriver koden ut en mening med f-strängar som kombinerar namnet, verbet "gillar" och favoritfärgen.

# EXERCISE
# Calculate age


birth_year = input('Födelseår: ')
print(type(birth_year))
birth_year = int(birth_year)  # Konvertera strängen till heltal
age = 2024 - birth_year
print(type(age))

print(f"Din ålder är {age} år.")

# Hur koden fungerar nu:

# 1. Koden frågar användaren om sitt födelseår med input().
# 2. Användarens indata (en sträng) lagras i variabeln birth_year.
# 3. Strängen birth_year konverteras till ett heltal med int().
# 4. Åldern beräknas genom att subtrahera det konverterade birth_year från 2024 och lagras i variabeln age.
# 5. Slutligen skriver koden ut en mening med f-strängar som visar användarens ålder.
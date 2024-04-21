# Ask a user their weight (in pounds), convert it to kg and print on the terminal.

weight_lbs = float(input('What is your weight in (lbs?) '))
weight_kg = weight_lbs * 0.45
print(f'Your weight in kg is: {weight_kg:.2f}')

# Förklaring

# 1 float(input("...")):
# Funktionen input() returnerar en sträng som standard.
# Vi använder float() för att konvertera användarens indata (antagligen ett nummer) till ett flyttal.
# Flyttal är lämpligare för att representera vikt eftersom det kan hantera decimaler.

# 2. f-sträng för utskrift:
# Vi använder en f-sträng för att formatera utdata och visa vikten i kilogram med två decimaler (.2f).

# Hur koden fungerar:

# 1. Koden frågar användaren efter vikten i pund med input().
# 2. Användarens indata konverteras till ett flyttal med float().
# 3. Vikten i kilogram beräknas genom att multiplicera vikten i pund med konverteringsfaktorn (0.45).
# 4. Slutligen skriver koden ut en mening med f-strängar som visar vikten i kilogram avrundad till två decimaler.


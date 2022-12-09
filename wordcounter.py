# Tar en textfil som parameter, räknar hur många ord det där, vilket är det mest förekommande ordet
import sys
try:
    textfil = sys.argv[1]
except:
    IndexError
    print(f'Du behöver ange en textfil som parameter')
    exit()

räknare = dict()
nummer = 0
vanligasteordet = ""

try:
    with open('textfil', "r") as f:
        for rad in f:
            ordlista = rad.split()
            for ord in ordlista:
                räknare[ord] = räknare.get(ord, 0) + 1

except UnicodeDecodeError:
    print(f'Kunde inte öppna filen')
    exit()

for nyckel in räknare:
    if räknare.get(nyckel) > nummer:
        nummer = räknare[nyckel]
        vanligasteordet = nyckel

print(f'Det vanligaste ordet är {vanligasteordet}. Det förekommer {nummer} gånger i filen.')

lista = []
for (k,v) in räknare.items():
    thistuple = (v, k)
    lista.append(thistuple)
lista.sort()
# skriver ut alla ord, ordnat efter hur vanliga de är
print(lista)
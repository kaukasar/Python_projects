# Läser upp innehållet i en loggfil vars namn och plats på servern varierar beroende på datum
#/var/trans/ut/aishpr/spar/2022-10/
#ais_intensivar.2022-10-21_000232.dat
import os
from datetime import datetime
import sys
#datum = input(f'Ange datum för PIV filen du vill öppna enligt formatet YYYY-MM-DD Tryck sedan på enter. ')
try:
    datum = sys.argv[1]
except:
    IndexError
    print(f'Du behöver ange ett datum som parameter enligt formatet "piv.py ÅÅÅÅ-MM-DD"')
    exit()

def validate(datum):
    try:
        if datum != datetime.strptime(datum, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False

if (validate(datum) == False):
    print(f'Du angav \"{datum}\". Felaktigt datumformat. Starta programmet igen.')
    exit()

katalog = str(datum[0:7])
sokvag = f'/var/trans/ut/aishpr/spar/{katalog}'
if (os.path.isdir(sokvag) == False):
    print(f'Det finns ingen fil till datalagret som är skapad den \"{datum}\".')
    exit()

prefixed = str([filename for filename in os.listdir(sokvag) if filename.startswith(f'ais_intensivar.{datum}')])
prefixed = prefixed.replace('[\'', "")
prefixed = prefixed.replace('\']', "")
fil = f'{sokvag}{prefixed}'
print(f'Öppnar filen \"{fil}\"\n')
f = open(fil, "r")
print(f.read())
f.close()

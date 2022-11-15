# Söker efter tillgängliga freerides på hertz mellan två städer
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
from inspect import cleandoc
import re
import sys
try:
    stad1 = sys.argv[1]
except:
    IndexError
    print(f'Ange enligt formatet "hertz.py stad1 stad2"')
    exit()
try:
    stad2 = sys.argv[2]
except:
    IndexError
    print(f'Ange enligt formatet "hertz.py stad1 stad2"')
    exit()
# Denna rad gör att certifikatfel ignoreras
ssl._create_default_https_context = ssl._create_unverified_context

r = urllib.request.urlopen('https://www.hertzfreerider.se/unauth/list_transport_offer.aspx')
dokument = BeautifulSoup(r, 'html.parser')
tagg1 = dokument('span', id=re.compile("^.*(offerHeader)$"))
tagg2 = dokument('span', id=re.compile("^.*(offerDate)$"))
tagg3 = dokument('span', id=re.compile("^.*(Label1)$"))
tagg4 = dokument('span', id=re.compile("^.*(offerDescription1)$"))
print("\n*** Följande freerides finns tillgängliga ***")
i = 0
inif = False
for element in tagg1:
    if stad1.lower() in element.text.lower() and stad2.lower() in element.text.lower():
        print(cleandoc(tagg1[i].text))
        print(f'Hämtas tidigast: {tagg2[i].text}')
        print(f'Lämnas senast: {tagg3[i].text}')
        print(tagg4[i].text)
        print("\n********************")
        inif = True
    i = i + 1
if(inif == False):
    print(f'Det fanns inga freerides mellan {stad1} och {stad2}.')
with open('input4.txt', 'r') as f:
    #rad = f.readline().strip()
    counter = 0
    totalsträng = ''
    lista = []
    for antalrader, rad in enumerate(f):
        rent = rad.strip()
        s = rent.replace('-', ',').split(',')
        totalsträng += f'{s[0]},{s[1]},{s[2]},{s[3]}'
        #print(s)
        a, b, c, d = int(s[0]), int(s[1]) ,int(s[2]), int(s[3])

        lista.append((a, b))
        lista.append((c, d))

        if (a <= c and b >= d) or (c <= a and d >= b):
            counter += 1

print(lista)
print(counter)
for element in lista:
    print(element[0])
    print(element[1])

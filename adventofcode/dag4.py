with open('input4.txt', 'r') as f:
    #rad = f.readline().strip()
    counter = 0
    lista = []
    for rad in f:
        rent = rad.strip()
        s = rent.replace('-', ',').split(',')
        #print(s)
        a, b, c, d = int(s[0]), int(s[1]), int(s[2]), int(s[3])

        #lista.append((a, b))
        #lista.append((c, d))
        #if (a <= c and b >= d) or (c <= a and d >= b): Detta tillhör del 1
        if b >= c and a <= d:
            counter += 1
            print(a, b, c, d)
            #print(f'{b} {c}')

print(counter)

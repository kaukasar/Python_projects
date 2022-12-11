with open('input1.txt', 'r') as f:
    innehåll = f.readlines()
    summa = 0
    räknare = 0
    dicten = {}
    totalLista = []
    for i in innehåll:
        if i != '\n':
            summa += int(i)
        else:
            dicten[räknare] = summa
            summa = 0
            räknare += 1
    summa = 0
    for nyckel in dicten:
        totalLista.append(dicten.get(nyckel))
        if dicten.get(nyckel) > summa:
            summa = dicten[nyckel]
            elf = nyckel
    totalLista.sort()
    print(f'Elf {elf} har flest kalorier, {summa} st.')
    print(f'De 3 Elf som har mest kalorier har tillsammans {totalLista[-1] + totalLista[-2] + totalLista[-3]} st.')
import string

with open('input3.txt', 'r') as f:
    prio = {}
    räknare = 1
    for letter in string.ascii_letters:
        prio[letter] = räknare
        räknare += 1

    for antalRader, _ in enumerate(f):
        pass
    antalRader += 1
    print(antalRader)

with open('input3.txt', 'r') as f:
    mellanlagring = set()
    räknare = 0
    while antalRader > 0:
        del1 = f.readline().strip()
        del2 = f.readline().strip()
        del3 = f.readline().strip()
        for char1 in del1:
            for char2 in del2:
                if char1 == char2:
                    mellanlagring.add(char1)
        for char3 in del3:
            for element in mellanlagring:
                if char3 == element:
                    gemensam = char3
        mellanlagring = set()
        räknare += prio.get(gemensam)
        antalRader -= 3
    print(räknare)

# Del 1 av uppgiften:
    """for rad in f:
    #  gemensam bokstav på 3 rader
        halva = int(len(rad.strip())/2)
        del1 = rad[0:halva]
        del2 = rad[halva:len(rad.strip())]
        print(del1, del2)
        gemensam = ''
        for char1 in del1:
            for char2 in del2:
                if char1 == char2:
                    gemensam = char1
                    break
        räknare += prio.get(gemensam)
    print(räknare)"""

with open('input6.txt', 'r') as f:
    startpekare = 0
    slutpekare = 14
    s = f.readline()
    for bokstav in s:
        if(len(set(s[startpekare:slutpekare]))) == 14:
            break
        if slutpekare == len(s):
            break
        startpekare += 1
        slutpekare += 1
print(slutpekare)
import re
totstr = []
totstr.append(['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q'])
totstr.append(['W', 'D', 'B', 'G'])
totstr.append(['F', 'W', 'R', 'T', 'S', 'Q', 'B'])
totstr.append(['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N'])
totstr.append(['M', 'P', 'D', 'V', 'F'])
totstr.append(['F', 'W', 'J'])
totstr.append(['L', 'N', 'Q', 'B', 'J', 'V'])
totstr.append(['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N'])
totstr.append(['J', 'S', 'Q', 'C', 'W', 'D', 'M'])
print(totstr)

def iLikeToMoveIt(mängd, från, till):
    while mängd > 0:
        a = totstr[från-1].pop(-mängd)
        #a = totstr[från - 1].pop() lösningen för del 1
        totstr[till-1].append(a)
        mängd -= 1

with open('input5.txt', 'r') as f:
    #rad = f.readline()
    #print(rad)
    for rad in f:
        renrad = re.sub('[a-zA-Z]', '', rad).strip().split('  ')
        iLikeToMoveIt(int(renrad[0]), int(renrad[1]), int(renrad[2]))

print(totstr)
for element in totstr:
    print(element[-1])
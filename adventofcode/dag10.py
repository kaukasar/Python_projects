indata = []
räknare = 0
x = 0
with open('input10.txt', 'r') as f:
    for rad in f:
        indata.append(rad.strip())

for i, element in enumerate(indata):
    if element == 'noop':
        räknare += 1
    if element.startswith('addx'):
        print(element[5:])

def kollaRäknareMatchar(r, xx):
    if r == 20 or r == 60 or r == 100 or r == 140 or r ==180 or r == 220:
        return True
    else:
        return False

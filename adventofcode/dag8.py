class matris:
    def __init__(self, m):
        self.matris = m
        self.utsiktRäknare = 0
        self.x, self.y = 0, 0

    def resetUtsikt(self):
        self.utsiktRäknare = 0
    def ökaUtsikt(self):
        self.utsiktRäknare += 1
    def getUtsikt(self):
        return self.utsiktRäknare

    def ettStegHöger(self):
        self.x += 1
    def ettStegVänster(self):
        self.x -= 1
    def ettStegUpp(self):
        self.y -= 1
    def ettStegNer(self):
        self.y += 1

    def lägstÅtHöger(self):
        if self.x == len(self.matris[0]) - 1:
            return True
        else:
            return False

    def lägstÅtVänster(self):
        if self.x == 0:
            return True
        else:
            return False

    def lägstUpp(self):
        if self.y == 0:
            return True
        else:
            return False

    def lägstNer(self):
        if self.y == len(self.matris) - 1:
            return True
        else:
            return False

    def getMatrisensBredd(self):
        return len(self.matris[0])
    def getMatrisensHöjd(self):
        return len(self.matris)

    def setPosition(self, x, y):
        self.x, self.y = x, y

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def getVärde(self, x, y):
        return self.matris[x][y]

def kollaUtsiktHöger(m):
    xx, yy = m.getX(), m.getY()
    while xx < m.getMatrisensBredd()-1:
        if m.matris[yy][m.x] > m.matris[yy][xx+1]:
            m.ökaUtsikt()
        else:
            m.ökaUtsikt()
            break
        xx += 1

def kollaUtsiktVänster(m):
    xx, yy = m.getX(), m.getY()
    while xx > 0:
        if m.matris[yy][m.x] > m.matris[yy][xx-1]:
            m.ökaUtsikt()
        else:
            m.ökaUtsikt()
            break
        xx -= 1

def kollaUtsiktNer(m):
    xx, yy = m.getX(), m.getY()
    while yy < m.getMatrisensHöjd()-1:
        if m.matris[m.y][xx] > m.matris[yy+1][xx]:
            m.ökaUtsikt()
        else:
            m.ökaUtsikt()
            break
        yy += 1

def kollaUtsiktUpp(m):
    xx, yy = m.getX(), m.getY()
    while yy > 0:
        if m.matris[m.y][xx] > m.matris[yy-1][xx]:
            m.ökaUtsikt()
        else:
            m.ökaUtsikt()
            break
        yy -= 1

indata = []
#koordinater = set()
with open('input8.txt', 'r') as f:
    for rad in f:
        indata.append([*rad.strip()])
matrix = matris(indata)
matrix.setPosition(0, 0)

dikten = {}
xx, yy = 0, 0

while matrix.getY() != matrix.getMatrisensHöjd():
    while matrix.getX() != matrix.getMatrisensBredd():
        kollaUtsiktHöger(matrix)
        tmp1 = matrix.getUtsikt()
        matrix.resetUtsikt()
        kollaUtsiktVänster(matrix)
        tmp2 = matrix.getUtsikt()
        matrix.resetUtsikt()
        kollaUtsiktUpp(matrix)
        tmp3 = matrix.getUtsikt()
        matrix.resetUtsikt()
        kollaUtsiktNer(matrix)
        tmp4 = matrix.getUtsikt()
        matrix.resetUtsikt()
        dikten[matrix.getX(), matrix.getY()] = tmp1*tmp2*tmp3*tmp4
        xx += 1
        matrix.setPosition(xx, yy)
    yy += 1
    xx = 0
    matrix.setPosition(0, yy)

max = 0
vinnare = ''
for nyckel in dikten:
    if dikten.get(nyckel) > max:
        max = dikten.get(nyckel)
        vinnare = str(nyckel)

print(vinnare, max) # uppgift 2, lösning (15, 45) 321975

# uppgift 1, lösning 1717
"""for y, element in enumerate(matris): # alla träd som syns från höger [OK]
    max = -1
    for x, _ in enumerate(element):
        if int(element[x]) > max:
            max = int(element[x])
            koordinater.add((x, y))

for y, _ in enumerate(matris): # alla träd som syns från vänster [OK]
    max = -1
    x = len(matris)
    for _ in matris:
        x -= 1
        if int(matris[y][x]) > max:
            max = int(matris[y][x])
            koordinater.add((x, y))

for x, _ in enumerate(matris): # alla träd som syns uppifrån [OK]
    max = -1
    for y, element in enumerate(matris):
        if int(element[x]) > max:
            max = int(element[x])
            koordinater.add((x, y))

for x, _ in enumerate(matris): # alla träd som syns nedifrån [OK]
    y = len(matris)
    max = -1
    for _ in matris:
        y -= 1
        if int(matris[y][x]) > max:
            max = int(matris[y][x])
            koordinater.add((x, y))"""

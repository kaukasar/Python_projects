class Node:
    def __init__(self, data, name, index):
        self.data = data
        self.name = name
        self.index = index
        self.child = []

#    def __repr__(self):
#        return (str(self.data), str(self.name))

    def findNode(self, searchedName):
        if self.name == searchedName:
            return self
        else:
            for child in self.child:
                result = child.findNode(searchedName)
                if result != None:
                    return result
        return None

def new_node(data, name):
    tmp = Node(data, name)
    return tmp

def traversal(root):
    if (root == None):
        return
    # Standard level order traversal, bredden-först sökning
    queue = []  # Skapar kön
    queue.append(root)  # Lägger in root elementet i kön, det enda som behöver läggas in manuellt

    while (len(queue) != 0): # Så länge kön != tom så betyder det att det finns noder vi ännu inte besökt
        itemsInQueue = len(queue)

        while (itemsInQueue > 0):
            dequeuedItem = queue.pop(0) # Plocka fram första noden i kön och skriv ut dess data
            print(dequeuedItem.name, dequeuedItem.data, end=' ')

            for children in range(len(dequeuedItem.child)): # Kontrollera om noden har några barn och lägg in dessa i kön.
                queue.append(dequeuedItem.child[children])
            itemsInQueue -= 1
        print()  # Print new line between two levels

root = Node(0, '/')
root.child.append(Node(10, 'a')), root.child.append(Node(20, 'b')), root.child.append(Node(30, 'c'))
root.child[0].child.append(Node(1, 'aa')), root.child[0].child.append(Node(2, 'bb'))

traversal(root)
print(root.findNode('b').data)
print(root.child[1].data)

#def printTree(noden):
#    while noden.isLeaf() == False:
#        print(noden.getData())
"""
$ cd /          root = Node(0, '/')
$ ls
dir fnsvfbzt    root.child.append(Node(0), 'fnsvfbzt')  lastname = 'fnsvfbzt'   index +=1
dir hqdssf      root.child.append(Node(0), 'hqdssf')    lastname = 'hqdssf'     index +=1
dir jwphbz      root.child.append(Node(0), 'jwphbz')    lastname = 'jwphbz'     index +=1
dir mhqs        root.child.append(Node(0), 'mhqs')      lastname = 'mhqs'       index +=1
132067 vjw      root.data = 132067                           
dir wbsph       root.child.append(Node(0), 'wbsph')     lastname = 'wbsph'      index +=1
$ cd fnsvfbzt                                           lastname = 'fnsvfbzt'   index = 0
$ ls
6215 sfwnts.hbj root.child[root.findNode(lastname).index].data = '6215'
$ cd ..
$ cd hqdssf                                             lastname = 'hqdssf'
$ ls
45626 cvcbmcm   root.child[root.findNode(lastname).index].data = '45626'
dir dlsmjsbz    
dir hqdssf
"""
#class Node(object):

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

    def get_child(self):
        return str(self.children)

    def add_child(self, obj):
        self.children.append(obj)

root = Node("roten")

a = Node("hej")
b = Node("japp")
c = Node(42)

root.add_child(a)
a.add_child(b)
root.add_child(c)

print(root.get_child())

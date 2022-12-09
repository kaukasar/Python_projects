#class Node(object):

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

    def get_child(self):
        return self.children

    def get_parent(self):
        pass

    def add_child(self, obj):
        self.children.append(obj)

root = Node("roten")

a = Node("hej")
b = Node("japp")
c = Node(42)
d = Node(True)

root.add_child(a.data)
a.add_child(b.data)
root.add_child(c.data)
c.add_child(d.data)

print(root.get_child())
print(c.get_child())
print(d.get_child())

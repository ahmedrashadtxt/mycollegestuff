class General_Tree_Node:
    def __init__(self, data):
        self.data = data
        self.child = None
        self.sibling = None

p = General_Tree_Node("P")
q = General_Tree_Node("Q")
r = General_Tree_Node("R")

a = General_Tree_Node("A")
b = General_Tree_Node("B")
c = General_Tree_Node("C")
d = General_Tree_Node("D")
e = General_Tree_Node("E")
f = General_Tree_Node("F")
g = General_Tree_Node("G")
h = General_Tree_Node("H")
i = General_Tree_Node("I")
j = General_Tree_Node("J")
k = General_Tree_Node("K")
l = General_Tree_Node("L")
m = General_Tree_Node("M")

root = p

p.child = q
q.sibling = r

q.child = a
a.sibling = b
r.child = c

a.child = d

b.child = e
e.sibling = f
f.sibling = g

c.child = h
h.sibling = i
i.sibling = j
j.sibling = k

d.child = l
l.sibling = m

print(root.child.child.data)
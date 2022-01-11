class Binary_Tree:

  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

a = Binary_Tree("A")
b = Binary_Tree("B")
c = Binary_Tree("C")
d = Binary_Tree("D")
e = Binary_Tree("E")
f = Binary_Tree("F")
g = Binary_Tree("G")

root = a

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

print(root.left.right.data)

def traverse_preorder(root):
  if root:
    print(root.data, end=" ")
    traverse_preorder(root.left)
    traverse_preorder(root.right)

traverse_preorder(root)

print()

def traverse_inorder(root):
  if root:
    traverse_inorder(root.left)
    print(root.data, end=" ")
    traverse_inorder(root.right)

traverse_inorder(root)

print()

def traverse_postorder(root):
  if root:
    traverse_postorder(root.left)
    traverse_postorder(root.right)
    print(root.data,end=" ")

traverse_postorder(root)

print()

def traverse_levelorder(root):
  queue = []
  queue.append(root)

  while(queue != []):
    node = queue.pop(0)
    print(node.data, end=" ")

    if(node.left != None):
      queue.append(node.left)

    if(node.right != None):
      queue.append(node.right)

traverse_levelorder(root)
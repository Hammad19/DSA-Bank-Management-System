class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


li = []
x = input("Enter the value to Search")


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        li.append(root.data),
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


root = Node('F')
root.left = Node('B')
root.left.left = Node('A')
root.left.right = Node('D')
root.left.right.left = Node('C')
root.left.right.right = Node('E')
root.right = Node('G')
root.right.right = Node('I')
root.right.right.left = Node('H')

printLevelOrder(root)

count = 0;
for y in li:
    count = count+1
    if y == x:
        print("Count = ")
        print(count)
        break

k = 0
while k < count:
    print(li[k])
    k += 1
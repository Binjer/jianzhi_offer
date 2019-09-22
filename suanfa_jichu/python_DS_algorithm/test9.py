# 树

# 列表表示的树
myTree = ['a',  # root
          ['b',  # left subtree
           ['d', [], []],
           ['e', [], []]],
          ['c',  # right subtree
           ['f', [], []],
           []]
          ]

print(myTree)
print("root", myTree[0])

print("左子树:", myTree[1])
print("右子树:", myTree[2])


# 使用列表作为树的函数来形式化树数据结构这个定义

def binaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


# 2. 使用节点和引用来表示树: 更接近于面向对象的编程实例
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def printexp(self):
        if self.leftChild:
            print("(", end=" ")
            self.leftChild.printexp()
        print(self.key, end=" ")
        if self.rightChild:
            print(")", end=" ")
            self.rightChild.printexp()


mytree = BinaryTree("a")
print(mytree.getRootVal())
print(mytree.getLeftChild())
mytree.insertLeft("b")
print(mytree.getLeftChild())
print(mytree.getLeftChild().getRootVal())
mytree.insertRight("c")
print(mytree.getRightChild())
print(mytree.getRightChild().getRootVal())

mytree.getRightChild().setRootVal("hello")
print(mytree.getRightChild().getRootVal())

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


# 表示树
def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == "(":
            currentTree.insertLeft("")
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i in ["+", "-", "*", "/"]:
            currentTree.setRootVal(i)
            currentTree.insertRight("")
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i not in ["+", "-", "*", "/", ")"]:
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent
        elif i == ")":
            currentTree = pStack.pop()
        else:
            raise ValueError

    return eTree


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder()  # defined and explained in the next section
pt.preorder()
pt.printexp()

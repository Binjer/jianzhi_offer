# 面试题32：不分行从上到下打印二叉树
# 同一层的节点按照从左到右的顺序打印

# 思路分析:
# 从上到下从左到右打印二叉树的规律为：
# 每打印一个节点的时候，如果该节点有子节点，就把该节点的子节点放到一个队列的末尾；
# 接下来从队列的头部取出最早进入队列的节点，重复前面的打印操作，直到队列中所有的节点都被打印出来。


class Solution(object):
    """
        返回一个一维列表,如[1,2,3,4]
    """

    def PrintFromTopToBottom(self, root):
        if not root:
            return []

        nodes = []
        nodes.append(root)
        res_val = []

        while len(nodes) > 0:
            curNode = nodes.pop(0)
            res_val.append(curNode.val)

            if curNode.left:
                nodes.append(curNode.left)
            if curNode.right:
                nodes.append(curNode.right)

        return res_val


# 也可以用collections模块中的deque实现, 效率更高
from collections import deque


class Solution2(object):
    """
        返回一个一维列表,如[1,2,3,4]
    """

    def PrintFromTopToBottom(self, root):

        if not root:
            return []

        nodes_queue = deque()
        nodes_queue.append(root)
        res_val = []

        while len(nodes_queue) > 0:
            curNode = nodes_queue.popleft()
            res_val.append(curNode.val)

            if curNode.left:
                nodes_queue.append(curNode.left)

            if curNode.right:
                nodes_queue.append(curNode.right)

        return res_val


# 题目变形1: 分行打印二叉树
# 这道题增加的难点在于为了将二叉树的每一层单独打印到一行里，我们需要找到判断一层节点是否打印完毕的条件
# 可以定义两个变量，一个表示当前层还没有打印的节点数目，另一个表示下一层节点的数目
class Solution11(object):
    """
        返回二维列表[[1,2],[4,5]],[1,2]表示第一层，[4,5]表示第二层
    """

    def Print(self, pRoot):
        if not pRoot:
            return []

        nodes = []
        nodes.append(pRoot)
        res_val = []

        # 表示当前层还没有打印的节点数，因为从根节点开始，所以初始化为1
        toBePrinted = 1
        # 表示下一层要打印的节点数
        nextLevel = 0
        temp = []

        while len(nodes) > 0:
            curNode = nodes.pop(0)
            temp.append(curNode.val)

            if curNode.left:
                nodes.append(curNode.left)
                nextLevel += 1  # 每遍历到一个子节点则下一层要打印的节点加1

            if curNode.right:
                nodes.append(curNode.right)
                nextLevel += 1  # 每遍历到一个子节点则下一层要打印的节点加1

            # 当前节点遍历完之后则该层的节点减1
            toBePrinted -= 1
            # 如果当前层节点打印完毕
            if toBePrinted == 0:
                res_val.append(temp)  # 把当前层的节点值的列表保存下来
                toBePrinted = nextLevel  # 当前需要打印的节点变成下一层的节点数
                nextLevel = 0  # 下一层节点数重置为0
                temp = []

        return res_val


class Solution12(object):
    """
        返回二维列表[[1,2],[4,5]],[1,2]表示第一层，[4,5]表示第二层
    """

    def Print(self, pRoot):

        """
        这种是更简洁的思路，把当前层的节点和下一层的节点用两个栈来保存，
        下面的变形题目之字形打印只需要添加一个判断方向的逻辑就可以了
        """

        if not pRoot:
            return []

        res_val = []
        nodes = [pRoot]

        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)

            res.append(curStack)
            nodes = nextStack

        return res_val


# 题目变形:2：之字形打印一颗二叉树
# 只需要在按行打印的基础上增加一个ltr的布尔值来判断即可，如果ltr为False，就将temp中的值逆序
class Solution21(object):
    def Print(self, pRoot):

        if not pRoot:
            return []

        nodes = []
        nodes.append(pRoot)
        res_val = []
        ltr = True

        # 表示当前层还没有打印的节点数，因为从根节点开始，所以初始化为1
        toBePrinted = 1
        # 表示下一层要打印的节点数
        nextLevel = 0
        temp = []

        while len(nodes) > 0:
            curNode = nodes.pop(0)
            temp.append(curNode.val)

            if curNode.left:
                nodes.append(curNode.left)
                nextLevel += 1  # 每遍历到一个子节点则下一层要打印的节点加1

            if curNode.right:
                nodes.append(curNode.right)
                nextLevel += 1  # 每遍历到一个子节点则下一层要打印的节点加1

            # 当前节点遍历完之后则该层的节点减1
            toBePrinted -= 1
            # 如果当前层节点打印完毕
            if toBePrinted == 0:
                ########################
                # TODO 增加这里的逻辑判断即可
                if ltr:
                    res_val.append(temp)  # 把当前层的节点值的列表保存下来
                else:
                    res_val.append(temp[::-1])
                ltr = not ltr
                ########################

                toBePrinted = nextLevel  # 当前需要打印的节点变成下一层的节点数
                nextLevel = 0  # 下一层节点数重置为0
                temp = []

        return res_val


# 书上的思路
class Solution22(object):
    def Print(self, pRoot):
        if not pRoot:
            return []

        res_val = []
        nodes = [pRoot]
        leftToRight = True

        while len(nodes) > 0:
            curStack, nextStack = [], []
            if leftToRight:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)

            res_val.append(curStack)
            nextStack.reverse()
            leftToRight = not leftToRight
            nodes = nextStack
        return res_val

    # 更简洁的写法
    def Print2(self, pRoot):

        if not pRoot:
            return []

        res_val = []
        nodes = [pRoot]
        leftToRight = True

        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)

            if not leftToRight:
                curStack.reverse()

            res_val.append(curStack)
            leftToRight = not leftToRight
            nodes = nextStack
        return res_val


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

s = Solution21()
res = s.Print(root)
print(res)

# 不分行从上到下打印二叉树
# 同一层的节点按照从左到右的顺序打印

# 思路分析:
# 构造一个辅助队列, 如果某个节点有子节点, 就把该节点的子节点放在队列的末尾.
# 遍历完成后, 再从队列头部依次打印元素


class Solution(object):
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []

        res = []
        res_val = []
        res.append(root)

        while len(res) > 0:
            curNode = res.pop(0)
            res_val.append(curNode.val)

            if curNode.left:
                res.append(curNode.left)
            if curNode.right:
                res.append(curNode.right)

        return res_val


# 也可以用collections模块中的deque实现, 效率更高
from collections import deque


class Solution2(object):
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []

        queue = deque()
        res_val = []
        queue.append(root)

        while len(queue) > 0:
            curNode = queue.popleft()
            res_val.append(curNode.val)

            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)

        return res_val


# 题目变形: 分行打印二叉树
class Solution3(object):
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here

        if not pRoot:
            return []

        res = []
        res.append(pRoot)
        res_val = []
        # 表示当前层还没有打印的节点数
        toBePrinted = 1
        # 表示下一层要打印的节点数
        nextLevel = 0
        temp = []

        while len(res) > 0:
            curNode = res.pop(0)
            temp.append(curNode.val)

            if curNode.left:
                res.append(curNode.left)
                nextLevel += 1

            if curNode.right:
                res.append(curNode.right)
                nextLevel += 1

            toBePrinted -= 1
            if toBePrinted == 0:
                res_val.append(temp)
                toBePrinted = nextLevel
                nextLevel = 0
                temp = []

        return res_val


class Solution4(object):
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here

        if not pRoot:
            return []
        res_val = []
        res = []
        res.append(pRoot)
        cur = 0

        while cur < len(res):
            last = len(res)
            temp = []

            while cur < last:
                node = res[cur]
                temp.append(node.val)
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                cur += 1
            res_val.append(temp)

        return res_val


# 之字形打印一颗二叉树
class Solution5(object):
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        res = []
        nodes = [pRoot]
        right = True

        while nodes:
            curStack, nextStack = [], []
            if right:
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

            res.append(curStack)
            nextStack.reverse()
            right = not right
            nodes = nextStack
        return res

    # 更简洁的写法
    def Print2(self, pRoot):
        # write code here
        if not pRoot:
            return []

        res = []
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

            res.append(curStack)
            leftToRight = not leftToRight
            nodes = nextStack
        return res


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

s = Solution5()
res = s.Print(root)
print(res)

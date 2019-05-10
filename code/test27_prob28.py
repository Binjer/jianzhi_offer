# 对称的二叉树
# 思路分析:
# 常规的前中后序遍历都是先遍历左节点再遍历右节点
# 如果我们能定义一种先遍历右节点, 再遍历左节点的遍历方式, 并与前面的遍历结果比较.
# 如果两者一样, 说明二叉树是对称的

class Solution(object):
    def isSymmetrical(self, pRoot):
        # write code here

        return self.isSymmert(pRoot, pRoot)

    def isSymmert(self, root1, root2):
        cur1 = root1
        cur2 = root2

        if cur1 is None and cur2 is None:
            return True

        if cur1 is None or cur2 is None:
            return False

        if cur1.val != cur2.val:
            return False

        return self.isSymmert(cur1.left, cur2.right) and self.isSymmert(cur1.right, cur2.left)

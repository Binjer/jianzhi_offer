# 面试题28：对称的二叉树

# 思路分析:
# 常规的前中后序遍历都是先遍历左节点再遍历右节点
# 如果我们能定义一种先遍历右节点, 再遍历左节点的遍历方式, 并与前面的遍历结果比较.
# 如果两者一样, 说明二叉树是对称的


# 一个指针根左右来遍历，另一个指针以跟右左来遍历，同时比较两个指针指向的值是否相同
# 考虑到左或右子树缺失的情况，将空指针也考虑进来
class Solution(object):

    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True  # 空树要按照题目要求返回值

        return self.isSymmertrical(pRoot, pRoot)

    def isSymmertrical(self, root1, root2):

        if root1 is None and root2 is None:  # 把空指针也考虑进来
            return True

        if root1 is None or root2 is None:  # 左右一个为空一个不为空则返回False
            return False

        if root1.val != root2.val:  # 左右值不一致则返回False
            return False

        return self.isSymmertrical(root1.left, root2.right) and self.isSymmertrical(root1.right, root2.left)

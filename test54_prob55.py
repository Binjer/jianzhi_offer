# 二叉树的深度
# 输入一棵二叉树的根结点，求该树的深度。
# 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 思路分析
# 递归实现, 十分方便.
# 如果一棵树只有一个节点, 那么它的深度为1
# 如果一棵树只有左子树没有右子树, 那么它的深度就等于左子树的深度加1
# 类似的, 如果一棵树只有右子树没有左子树, 那么它的深度就等于右子树的深度加1
# 既有左子树又有右子树时, 深度等于左右子树中较大的深度加1(包含了所有情况)
class Solution:
    def treeDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)

        # return left + 1 if left > right else right + 1
        return max(left, right) + 1


# 题目二: 平衡二叉树
# 很容易想到的一个思路是利用上面求树的深度的函数.
# 当遍历到一个节点时, 判断该节点的左右子树的深度相差是不是超过1.
# 遍历每一个节点并判断即可
class Solution21(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced()

    def treeDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)

        return max(left, right) + 1


# 每个节点只需要遍历一次的解法
class Solution22(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        balanced, depth = self.balancedCore(root)

        return balanced

    def balancedCore(self, root, depth=0):
        if not root:
            depth = 0
            return True, depth

        # 找到左节点
        fLeft, left = self.balancedCore(root.left)
        # 找到右节点
        fRight, right = self.balancedCore(root.right)

        # 判断左右节点是否是平衡的, 是的话返回到其父节点
        if fLeft and fRight:
            if abs(left - right) <= 1:
                depth = max(left, right) + 1
                return True, depth

        return False, depth

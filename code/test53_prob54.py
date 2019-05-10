# 二叉搜索树的第k大节点

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解题思路: 就是中序遍历
class Solution(object):
    def kthNode(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: TreeNode
        """
        if not root:
            return -1

        res = []
        self.inOrder(root, res)

        return res[k - 1]

    def inOrder(self, root, res):
        if not root:
            return []

        self.inOrder(root.left, res)
        res.append(root)
        self.inOrder(root.right, res)
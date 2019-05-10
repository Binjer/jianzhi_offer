# 树的子结构

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.iseuqual(pRoot1, pRoot2)
            # 判断左子树中是否包含B树结构
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            # 判断右子树中是否包含B树结构
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)

        return result

    def iseuqual(self, root1, root2):
        # 如果B树为空，那么可以算B是A的子结构
        if not root2:
            return True
        # 如果A树空，而B树不空，那么B不是A的子结构
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        # 根节点值相同，在判断左右子树是否都相同
        return self.iseuqual(root1.left, root2.left) and self.iseuqual(root1.right, root2.right)




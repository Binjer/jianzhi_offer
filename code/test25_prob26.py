# 面试题26：树的子结构
# 输入两棵二叉树A和B，判断B是不是A的子结构。约定空树不是任何一个树的子结构

# 思路分析：首先在A中找到值与B的根节点的值相等的节点，
#          然后判断找到的节点是不是含有和B一样的结构；
#          如果是则返回True， 不是则需要继续在A中遍历找到与B的根节点的值相等的节点，依次重复判断


# 树节点定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def HasSubtree(self, pRoot1, pRoot2):

        result = False

        if pRoot1 and pRoot2:
            # 这里有一个细节是计算机是如何判定两个小数相等的，计算机内表示小数时都有误差，
            # 因此判断两个小数是否相等，是判断它们的差的绝对值是不是小于某个很小的阈值，是的话就判定它们相等
            if pRoot1.val == pRoot2.val:
                result = self.iseuqual(pRoot1, pRoot2)  # 注意函数能执行这一步意味着A中至少有一个节点的值与B的根节点的值相同

            # 判断左子树中是否包含B树结构
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            # 判断右子树中是否包含B树结构
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)

        return result

    def iseuqual(self, root1, root2):
        # 如果B的子树为空，那么可以算B是A的子结构
        if not root2:
            return True
        # 如果A的子树为空，而B的子树不为空，那么B不是A的子结构
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        """前面三个if主要是再判断子结构中生效的"""

        # 根节点值相同，再判断左右子树是否都相同
        return self.iseuqual(root1.left, root2.left) and self.iseuqual(root1.right, root2.right)

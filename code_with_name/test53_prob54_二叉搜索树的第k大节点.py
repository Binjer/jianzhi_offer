# 面试题54：二叉搜索树的第k大节点

# 名词解释：二叉搜索树左节点的值都比根节点的值小，右节点的值都比根节点的值大，中序遍历就是升序排列

# 二叉树节点定义如下
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 解题思路: 就是中序遍历
class Solution(object):
    def kthNode(self, root, k):

        if not root or k<= 0:
            return None

        res = []
        self.inOrder(root, res)  # res是升序排列的数组

        if len(res) < k:
            return None

        return res[-k]

    def inOrder(self, root, res):
        if not root:
            return []

        self.inOrder(root.left, res)
        res.append(root)
        self.inOrder(root.right, res)


# 下面是牛客网上的题目，是求第k小的节点
class Solution1(object):
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code_with_name here
        if not pRoot:
            return None

        if k <= 0:
            return None

        res = []
        self.inOrder(pRoot, res)

        if len(res) < k:
            return None

        return res[k - 1]

    def inOrder(self, pRoot, res):

        if not pRoot:
            return []

        self.inOrder(pRoot.left, res)
        res.append(pRoot)
        self.inOrder(pRoot.right, res)

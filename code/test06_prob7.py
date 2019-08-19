# 面试题7: 重建二叉树
# 根据前序遍历结果和中序遍历结果重建二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 用递归解决
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):

        if not pre or not tin:
            return None

        # 重建根节点
        root = TreeNode(pre[0])
        # 找到根节点在中序遍历序列中的位置
        root_index_in_tin = tin.index(pre[0])

        # 递归重建左子树和右子树
        root.left = self.reConstructBinaryTree(pre[1:root_index_in_tin + 1], tin[:root_index_in_tin])
        root.right = self.reConstructBinaryTree(pre[root_index_in_tin + 1:], tin[root_index_in_tin + 1:])

        return root

    # 已知中序遍历结果和后序遍历结果
    def reConstructBinaryTree2(self, post, tin):

        if not post or not tin:
            return None

        root = TreeNode(post[-1])
        index = tin.index(post[-1])

        root.left = self.reConstructBinaryTree2(post[:index], tin[:index])
        root.right = self.reConstructBinaryTree2(post[index:-1], tin[index + 1:])

        return root

    # 已知前序遍历结果和后序遍历结果
    def reConstructBinaryTree3(self, pre, post):

        if not post or not pre:
            return None

        root = TreeNode(pre[0])
        left_root = TreeNode(pre[1])
        index = post.index(pre[1])

        root.left = self.reConstructBinaryTree2(pre[1:index + 2], post[:index + 1])
        root.right = self.reConstructBinaryTree2(pre[index + 2:], post[index + 1:-1])

        return root

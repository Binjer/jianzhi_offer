# 重建二叉树

# 根据前序遍历结果和中序遍历结果重建二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None

        root = TreeNode(pre[0])
        root_index_in_tin = tin.index(pre[0])

        root.left = self.reConstructBinaryTree(pre[1:root_index_in_tin + 1], tin[:root_index_in_tin])
        root.right = self.reConstructBinaryTree(pre[root_index_in_tin + 1:], tin[root_index_in_tin + 1:])

        return root

    # 已知中序遍历结果和后序遍历结果
    def reConstructBinaryTree2(self, post, tin):
        # write code here
        if not post or not tin:
            return None

        root = TreeNode(post[-1])
        index = tin.index(post[-1])

        root.left = self.reConstructBinaryTree2(post[:index], tin[:index])
        root.right = self.reConstructBinaryTree2(post[index:-2], tin[index + 1:])

        return root

    # 已知前序遍历结果和后序遍历结果
    def reConstructBinaryTree3(self, pre, post):
        # write code here
        if not post or not pre:
            return None

        root = TreeNode(pre[0])
        left_root = TreeNode(pre[1])
        index = post.index(pre[1])

        root.left = self.reConstructBinaryTree2(pre[1:index + 2], post[:index + 1])
        root.right = self.reConstructBinaryTree2(pre[index + 2:], post[index + 1:-2])

        return root

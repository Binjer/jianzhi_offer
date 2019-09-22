# 面试题37：序列化和反序列化二叉树

# 实现两个函数，用来序列化和反序列化二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 序列化
    def Serialize(self, root):
        # 按照前序遍历的顺序序列化
        if not root:
            return "$"
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    # 反序列化
    def Deserialize(self, s):

        li = s.split(",")
        return self.DeserializeCore(li)

    def DeserializeCore(self, li):
        if len(li) <= 0:
            return None
        root = None
        val = li.pop(0)
        if val != "$":
            root = TreeNode(int(val))
            root.left = self.DeserializeCore(li)
            root.right = self.DeserializeCore(li)
        return root

# 另一种思路是先把一棵树变成前序遍历序列和中序遍历序列, 反序列化就是二叉树的重建
# 这种方法的缺点是二叉树中不能有重复的值

# 面试题34：二叉树中和为某一值的路径

# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
# 从树的根节点开始往下一直到叶节点所经过的节点形成一条路径


# 书上的思路
class Solution1(object):
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):

        path = []
        pathAll = []
        if not root:
            return pathAll
        currentSum = 0

        self.FindPathnew(root, expectNumber, path, pathAll, currentSum)

        return pathAll

    def FindPathCore(self, root, expectNumber, path, pathAll, currentSum):

        path.append(root.val)
        currentSum += root.val

        # 判断是否是叶子节点
        isLeaf = root.left is None and root.right is None

        if currentSum == expectNumber and isLeaf:
            onepath = []
            for val in path:
                onepath.append(val)
            pathAll.append(onepath)
            # pathAll.append(copy.deepcopy(path)) # 也可借助copy模块的deepcopy来实现一条路径的复制
        if currentSum < expectNumber:
            if root.left is not None:
                self.FindPathCore(root.left, expectNumber, path, pathAll, currentSum)

            if root.right is not None:
                self.FindPathCore(root.right, expectNumber, path, pathAll, currentSum)
        path.pop()


# 按照前序遍历的顺序遍历整棵树，不断修改expectNumber的值即可
class Solution2(object):
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):

        if not root:
            return []

        # 如果只有根节点或者找到了叶子节点，则将其值返回
        if root.val == expectNumber and not root.left and not root.right:
            return [[root.val]]

        # 如果不是叶子节点，则分别对节点的左子树和右子树进行递归，注意修改expectNumber的值
        res = []
        left = self.FindPath(root.left, expectNumber - root.val)
        # print("left", left)
        right = self.FindPath(root.right, expectNumber - root.val)
        # print("right", right)

        for item in left + right:  # 这里如果left+right=[],则循环体内的代码不会被执行
            print("执行了吗？", root.val)
            res.append([root.val] + item)
        return res


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)

    s = Solution2()
    res = s.FindPath(root, 23)
    print(res)

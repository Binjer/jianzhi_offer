# 二叉树中和为某一值的路径

class Solution(object):
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []

        res = []
        currentSum = 0
        path = []

        def FindPathCore(root, expectNumber, path, currentSum):
            currentSum += root.val
            path.append(root.val)

            isLeaf = (root.left is None and root.right is None)
            if isLeaf and currentSum == expectNumber:
                onepath = []
                for val in path:
                    onepath.append(val)
                res.append(onepath)

            if currentSum < expectNumber:
                if root.left:
                    FindPathCore(root.left, expectNumber, path, currentSum)
                if root.right:
                    FindPathCore(root.right, expectNumber, path, currentSum)
            path.pop()

        FindPathCore(root, expectNumber, path, currentSum)

        return res

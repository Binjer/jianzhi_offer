# 一、递归


# 1.递归，说白了就是就是程序的自身调用，把一个大的问题转化为和小的和原问题相似的问题来求解。
# 2.递归算法必须要有一个出口，也就是递归结束的条件一定要明确


# 题目一：
def fibonacci(n):
    """
    斐波那契数列可以用递归来解决；
    可能会出现RecursionError:maximum recursion depth exceeded in comparison
    """

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(10000))

# 因此我们基于递归来分析问题，但常常基于循环来编写代码
def fibonacci1(n):
    """
    循环解法
    """

    if n == 1:
        return 1
    elif n == 2:
        return 1

    f1 = 1
    f2 = 1
    for i in range(3, n + 1):
        fn = f1 + f2

        f1 = f2
        f2 = fn

    return f2


# print(fibonacci1(5000))


# 题目二
# 数据结构中树最常用到递归的思想
# leetcode938:二叉搜索树的范围和
# 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
# 二叉搜索树保证具有唯一的值。
class Solution(object):
    def rangeSumBST(self, root, L, R):

        # 基础递归思路
        # if root:
        #     if (L <= root.val <= R) or (R <= root.val <= L):
        #         return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        #     else:
        #         return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        # else:
        #     return 0

        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                # 如果某个节点的值大于L但是不小于R，那么它右节点的所有值都不小于R，我们只要遍历它的左子树就可以了
                if L < node.val:
                    dfs(node.left)
                # 如果某个节点的值小于R但是不大于L，那么它左节点的所有值都不大于L，我们只要遍历它的右子树就可以了
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans

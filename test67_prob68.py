# 树中两个节点的最低公共祖先

# 1. 假如树是二叉搜索树
# 二叉树的问题，一般要用递归解决。
# 如果p，q都在root的左子树，则解就在左子树，反之解在右子树。
# 如果p和q一个在左子树，一个在右子树，那么解就是root。

# 这里无须区分到底找到的是p还是q，只要找到一个即可返回该结点。
# 在某结点的左子树上找到了p，不继续深入查找了，在该结点右子树未找到q，题目保证一定有祖先，所以q一定在p的后代里。
# 遍历到空节点表明没找到，遍历到p或者q就说明找到了，这是递归的两种边界情况。
# 递归的主体如上所述，只在左子树上找到了则返回左子树，两棵子树都找到了则返回root。
# 由于递归的性质，遍历到解了才开始回溯，所以返回的就是最低公共祖先
class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left is None:
            return right
        else:
            return left


# 2. 如果是普通的树， 但是有指向父节点的指针。
# 可以转换为两个链表的第一个公共节点的问题， 见题目52.
# 可以借助栈来解决；
# 也可以使用遍历长度的技巧性方法来解决。

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root or not p or not q:
            return None

        s1 = []
        s2 = []

        while p != root:
            s1.append(p)
            p = p.parent

        while q != root:
            s2.append(q)
            q = q.parent

        # 要找到最后一个相同的节点
        res = None
        while len(s1) > 0 and len(s2) > 0:
            tmp1 = s1.pop()
            tmp2 = s2.pop()
            if tmp1 == tmp2:
                res = tmp1
            else:
                break

        return res


# 3.如果树是一颗普通的树（不一定是二叉树）， 并且树中的节点没有指向父节点的指针。
# 从上到下遍历树找到一个节点它自己的子树中包含p、q两个节点， 而它的子节点不包含， 那么这个节点就是两个节点的最低公共祖先。

# 上面的思路需要重复遍历很多节点， 因此可以借助辅助栈，保存根节点到p，q的两条路径，找到路径中的最后一个公共节点。
# 这与前面的题目34思路类似， 主要考察的思想是如何遍历一棵树中的路径。
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        s1 = []
        s2 = []
        self.getNodePath(root, p, s1)
        self.getNodePath(root, p, s2)

        # res = None
        # while len(s1) > 0 and len(s2) > 0:
        #     # 这点可以看出用双端队列实现更有效率
        #     tmp1 = s1.pop(0)
        #     tmp2 = s2.pop(0)
        #     if tmp1 == tmp2:
        #         res = tmp1
        #     else:
        #         break
        # return res

        # 如果就是用栈来解决
        res = None
        # 先把两个栈的长度变为一致
        while len(s1) != len(s2):
            if len(s1) > len(s2):
                s1.pop()
            else:
                s2.pop()

        while s1[-1] != s2[-1]:
            s1.pop()
            s2.pop()

        # 如果题目中说明必有祖先的话这里的判断是不必要的。
        if len(s1) > 0:
            return s1[-1]

    def getNodePath(self, root, node, path):
        if root.val == node.val:
            return 1
        path.append(root)

        # 这里实际上要看树节点的定义是什么样的
        if self.getNodePath(root.left, node, path) == 1:
            return 1

        if self.getNodePath(root.right, node, path) == 1:
            return 1

        # 如果找到叶节点还没找到要找的值， 弹出叶节点，回溯到其父节点
        path.pop()
        return 0

# 如果是普通的二叉树， 还有一种解题思路：
# 如果一个结点为根，另一个结点无论在什么地方它们的最低公共祖先一定为根结点。
# 如果一个结点在左树，另一个结点在右树，那么它的最低公共祖先一定是根节点。
# 如果两个结点都在左树，以子问题在左树查找。
# 如果两个结点都在右树，以子问题在右树查找。

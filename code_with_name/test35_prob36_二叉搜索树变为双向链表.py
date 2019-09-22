# 面试题36：二叉搜索树与双向链表


# 分析：如果二叉搜索树定义为左节点的值都比根节点小，右节点的值都比根节点的大，那么此时它的中序遍历序列是升序排列的
# 一种简单的思路是先获得二叉搜索树的中序遍历结果, 然后调整指针指向
# 需要额外的O(n)空间


class Solution1(object):
    def Convert(self, pRootOfTree):

        root = pRootOfTree
        if not root:
            return

        self.attr = []
        self.InOrder(root)

        # for i, v in enumerate(self.attr[:-1]):
        #     self.attr[i].right = self.attr[i + 1]
        #     self.attr[i + 1].left = v

        for i in range(len(self.attr) - 1):
            self.attr[i].right = self.attr[i + 1]
            self.attr[i + 1].left = self.attr[i]

        return self.attr[0]

    def InOrder(self, root):
        if not root:
            return
        self.InOrder(root.left)
        self.attr.append(root)
        self.InOrder(root.right)


# 剑指offer上的思路
# 递归:
# 将特定节点(根节点)的左指针指向其左子树中的最右子节点，
# 将其右指针指向其右子树中的最左子节点.
# 依次递归，调整好全部节点的指针指向。
class Solution2(object):
    # 书上的思路
    def Convert(self, pRootOfTree):

        self.pLastNodeInList = None
        self.ConvertNode(pRootOfTree)

        pHeadOfList = self.pLastNodeInList

        while pHeadOfList is not None and pHeadOfList.left is not None:
            pHeadOfList = pHeadOfList.left

        return pHeadOfList

    def ConvertNode(self, pRootOfTree):

        pNode = pRootOfTree
        if pNode is None:
            return

        if pNode.left is not None:
            self.ConvertNode(pNode.left)

        pNode.left = self.pLastNodeInList
        if self.pLastNodeInList is not None:
            self.pLastNodeInList.right = pNode

        self.pLastNodeInList = pNode
        if pNode.right is not None:
            self.ConvertNode(pNode.right)


# 另外一种思路
class Solution3(object):

    def Convert(self, pRootOfTree):

        root = pRootOfTree
        if not root:
            return

        # 这是为了找到左子树中的最左叶节点, 也就是双向链表的首个元素
        pHead = root
        while pHead.left:
            pHead = pHead.left

        # 调整节点指针指向
        self.Core(root)

        return pHead

    def Core(self, root):
        # 到达了叶节点
        if not root.left and not root.right:
            return

        if root.left:
            # 左子树的根节点
            preRoot = root.left
            # 找到左子树的最左叶节点
            self.Core(root.left)

            # 调整节点指针指向
            while preRoot.right:
                preRoot = preRoot.right
            preRoot.right = root
            root.left = preRoot

        if root.right:
            # 右子树的根节点
            nextRoot = root.right

            # 右子树的最右节点
            self.Core(root.right)
            while nextRoot.left:
                nextRoot = nextRoot.left
            nextRoot.left = root
            root.right = nextRoot


# 最后贴一个博客上看来的解法
# https://blog.csdn.net/u010005281/article/details/79657259
# 应该是见到的最简单的思路了
class Solution4(object):
    def __init__(self):
        self.listHead = None  # 用来记录双向链表头节点最后返回
        self.listTail = None  # 记录当前已经转换好的双向链表的尾节点

    def Convert(self, pRootOfTree):

        if pRootOfTree is None:
            return

        self.Convert(pRootOfTree.left)  # 中序遍历(左)

        # 其实就是用if——else这部分代码代替了中序遍历中对根节点的处理
        if self.listHead is None:  # 这个if语句只在中序遍历到第一个节点时有用
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree  # 这三行是更改指针指向的代码
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree  # 每次指针调整完毕之后，尾节点就往后移动(按照中序的顺序移动)

        self.Convert(pRootOfTree.right)  # 中序遍历(右)

        return self.listHead

# def InOrder(root):
#     if not root:
#         return
#     InOrder(root.left)
#     res.append(root.val)
#     InOrder(root.right)
#
#     return res
#
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(12)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(7)
#
# # 下面是如何得到一棵树的中序遍历序列
# res = []
# print(InOrder(root))

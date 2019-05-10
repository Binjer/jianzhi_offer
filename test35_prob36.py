# 二叉搜索树与双向链表

# 一种简单的思路是先获得二叉搜索树的中序遍历结果, 然后调整指针指向
# 需要额外的O(n)空间
class Solution(object):
    def Convert(self, pRootOfTree):
        # write code here
        root = pRootOfTree
        if not root:
            return

        self.attr = []
        self.InOrder(root)

        for i, v in enumerate(self.attr[:-1]):
            self.attr[i].right = self.attr[i + 1]
            self.attr[i + 1].left = v

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
    def Convert(self, pRootOfTree):
        # write code here
        pLastNodeInList = None
        self.ConvertNode(pRootOfTree, pLastNodeInList)

        pHeadOfList = pLastNodeInList

        while pHeadOfList is not None and pHeadOfList.left is not None:
            pHeadOfList = pHeadOfList.left

        return pHeadOfList

    def ConvertNode(self, pRootOfTree, pLastNodeInList):
        pNode = pRootOfTree
        if pNode is None:
            return

        cur = pNode
        if cur.left is not None:
            self.ConvertNode(cur.left, pLastNodeInList)

        cur.left = pLastNodeInList
        if pLastNodeInList is not None:
            pLastNodeInList.right = cur

        pLastNodeInList = cur
        if cur.right is not None:
            self.ConvertNode(cur.right, pLastNodeInList)

    def Convert1(self, pRootOfTree):
        # write code here
        root = pRootOfTree
        if not root:
            return

        # 这是为了找到左子树中的最左叶节点, 也就是双向链表的首个元素
        pHead = root
        while pHead.left:
            pHead = pHead.left

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







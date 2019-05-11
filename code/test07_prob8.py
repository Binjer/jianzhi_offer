# 面试题8: 二叉树的下一个节点
# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution(object):
    def GetNext(self, pNode):

        if not pNode:
            return

        # 如果该节点的右子树不为空, 那么下一个节点为节点右子树的最左子节点
        if pNode.right is not None:
            cur = pNode.right
            while cur.left is not None:
                cur = cur.left
            return cur
        # 如果节点没有右子树, 并且它还是父节点的右子节点.
        # 需要沿着指向父节点的指针一直遍历, 直到找到一个是其父节点的左子节点的节点
        # 它的下一节点就是我们要找的节点
        elif pNode.next is not None and pNode.next.right == pNode:
            while pNode.next is not None and pNode.next.left != pNode:
                pNode = pNode.next
            return pNode.next
        # 如果节点右子树为空, 它还是父节点的左子节点, 那么下一个节点就是它的父节点
        else:
            return pNode.next

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


# 给定一颗二叉树和一个节点, 如何找出中序遍历中下一个节点. 已知节点指向左右子节点和父节点的三个指针
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return

        elif pNode.right is not None:
            cur = pNode.right
            while cur.left is not None:
                cur = cur.left
            return cur
        # 这里面已经包含了pNode.right为空
        elif pNode.next is not None and pNode.next.right == pNode:
            while pNode.next is not None and pNode.next.left != pNode:
                pNode = pNode.next
            return pNode.next
        else:
            return pNode.next

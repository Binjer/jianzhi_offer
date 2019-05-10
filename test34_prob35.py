# 复杂链表的复制
# 在复杂链表中, 每个节点除了有一个next指针指向下一个节点,
# 还有一个sibling指针指向链表中的任意节点或者None


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        # 先把每个节点都克隆一遍
        self.doubleClone(pHead)

        # 每个克隆的节点的random指针, 指向它本体的random指针的克隆节点
        self.cloneSibling(pHead)

        # 再把链表拆分开来, 奇数项是原来的链表; 偶数项是复制完成的链表
        return self.splitTwoLinkedlist(pHead)

    def doubleClone(self, pHead):
        pNode = pHead
        while pNode is not None:
            cloneNode = RandomListNode(0)
            cloneNode.label = pNode.label
            cloneNode.next = pNode.next

            pNode.next = cloneNode
            pNode = cloneNode.next

    def cloneSibling(self, pHead):
        pNode = pHead
        while pNode:
            pCloneNode = pNode.next
            if pNode.random is not None:
                pCloneNode.random = pNode.random.next
            pNode = pCloneNode.next

    def splitTwoLinkedlist(self, pHead):
        pNode = pHead
        pCloneHead = pNode.next

        pCloneNode = pNode.next
        pNode.next = pCloneNode.next
        pNode = pNode.next

        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next

        return pCloneHead


# 递归法
class Solution2(object):
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        newHead = RandomListNode(0)
        pHead.next = newHead
        newHead.next = self.Clone(pHead.next)

        return newHead

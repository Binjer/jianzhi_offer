# 面试题35：复杂链表的复制

# 在复杂链表中, 每个节点除了有一个next指针指向下一个节点,
# 还有一个sibling指针指向链表中的任意节点或者None


# 这是牛客网上的定义
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# 书上的思路：分解为三个小步骤
# 第一步：将每个节点都复制一遍，并用原来的节点指向复制的节点
# 第二步：每个复制的节点的random应该指向原来节点的下一个位置(即原来节点的复制节点)
# 第三步：将2n链表拆成两个，奇数位置的节点连接起来就是原链表，偶数位置的节点连接起来就是复制的链表
class Solution(object):
    # 返回 RandomListNode
    def Clone(self, pHead):

        if not pHead:
            return pHead

        self.doubleClone(pHead)
        self.setRandom(pHead)
        return self.splitTwoLinkedList(pHead)

    def doubleClone(self, pHead):
        while pHead is not None:
            cloneNode = RandomListNode(pHead.label)
            cloneNode.next = pHead.next

            pHead.next = cloneNode
            pHead = cloneNode.next

    def setRandom(self, pHead):
        while pHead is not None:
            cloneNode = pHead.next
            if pHead.random is not None:
                cloneNode.random = pHead.random.next
            pHead = cloneNode.next

    def splitTwoLinkedList(self, pHead):

        pCloneHead = pHead.next  # 先保存克隆链表的头结点

        pCloneNode = pHead.next  # 游标指向第一个克隆的节点
        pHead.next = pCloneNode.next
        pHead = pHead.next

        while pHead is not None:
            pCloneNode.next = pHead.next

            pCloneNode = pCloneNode.next
            pHead.next = pCloneNode.next
            pHead = pHead.next

        return pCloneHead


# 递归法
class Solution2(object):
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return pHead

        # 先复制第一个节点
        p = RandomListNode(pHead.label)
        p.random = pHead.random

        # 递归复制剩下的节点，并与前面的节点连接起来
        p.next = self.Clone(pHead.next)

        return p

# if __name__ == '__main__':
#     pHead = RandomListNode(10)
#     pHead.next = RandomListNode(5)
#
#     print(pHead.next)
#     p = pHead
#     print(p.next)
#
#     # 当这里修改了节点的指向时，也就相当于修改了pHead的指向，那么pHead原本指向的5就找不到了
#     p.next = RandomListNode(8)
#     print(p.next)
#     print(pHead.next)

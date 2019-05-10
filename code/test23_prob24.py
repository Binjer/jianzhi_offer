# 翻转链表: 无头节点的情况
class Solution11(object):
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here

        if pHead is None or pHead.next is None:
            return pHead

        prev = None
        cur = pHead

        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


# 递归解决无头节点的逆序
class Solution12(object):
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here

        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return newHead


# 有头结点的情况: 就地逆序的话头结点需要特殊处理.即要把第一个数据节点变成尾节点
class Solution21(object):
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here

        if pHead is None or pHead.next is None:
            return pHead

        cur = pHead.next
        pNext = cur.next
        cur.next = None

        pre = cur
        cur = pNext
        while cur.next is not None:
            pNext = cur.next
            cur.next = pre
            pre = cur
            cur = cur.next

        cur.next = pre
        pHead.next = cur

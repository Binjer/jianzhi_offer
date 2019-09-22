# 面试题24：翻转链表


# 翻转链表主要包括原地逆转、递归和插入法这几种思路
# 有时还要注意题目要求中链表有无头节点
# 个人比较推荐插入法和递归法

# 1.无头节点的情况
# 1.1.插入法：从第二个节点开始，依次将其插入到前面(有点类似先出链表再从头插入链表)
class Solution11(object):
    # 返回ListNode
    def ReverseList(self, pHead):

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


# 1.2.递归解决无头节点的逆序
class Solution12(object):
    # 返回ListNode
    def ReverseList(self, pHead):

        if not pHead or not pHead.next:
            return pHead
        else:
            # 反转后面的节点
            newHead = self.ReverseList(pHead.next)
            # 把当前遍历的节点加到后面节点逆序后链表的尾部
            pHead.next.next = pHead
            pHead.next = None
            return newHead


# 2.有头结点的情况:
# 2.1.就地逆序的话头结点需要特殊处理.即要把第一个数据节点变成尾节点
class Solution21(object):
    # 返回ListNode
    def ReverseList(self, pHead):

        if pHead is None or pHead.next is None:
            return pHead

        cur = pHead.next  # 第一个数据节点(反转后是最后一个节点)
        pNext = cur.next  # 第二个数据节点
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

        return pHead


# 2.2.递归法
class Solution22(object):
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None:
            return

        # 获取链表第一个(数据)节点
        firstNode = pHead.next
        # 对链表进行逆序
        newHead = self.RecursiveCore(firstNode)
        # 将头节点指向逆序后链表的第一个节点
        pHead.next = newHead

        return newHead

    def RecursiveCore(self, pHead):

        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.RecursiveCore(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
        return newHead


# 2.3.插入法
class Solution23(object):
    # 返回ListNode
    def ReverseList(self, pHead):

        if pHead is None or pHead.next is None:
            return pHead

        pre = pHead.next  # 指向第一个数据节点
        cur = pHead.next.next  # 指向第二个数据节点
        pre.next = None  # 第一个数据节点成为反转后链表的最后一个节点

        while cur is not None:
            temp = cur.next  # 保存下一个节点的信息
            cur.next = pre
            pre = cur
            cur = temp

        return pre

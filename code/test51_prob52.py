# 两个链表的第一个公共节点


# 解法一:
# 借助两个栈,先把两个链表的节点依次入栈
# 依次弹出栈顶元素, 直到最后一个相同的元素为止
class Solution1(object):
    def findFirstCommonNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        s1 = []
        s2 = []

        p1 = headA
        p2 = headB

        while p1:
            s1.append(p1)
            p1 = p1.next

        while p2:
            s2.append(p2)
            p2 = p2.next

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


# 解法二:
# 先遍历两个链表得到各自长度
# 在长链表上先走m-n步
# 一起走到尾部, 看是否有相等的节点
class Solution2(object):
    def findFirstCommonNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        p1 = headA
        p2 = headB

        l1 = self.getLen(p1)
        l2 = self.getLen(p2)

        if l1 > l2:
            for i in range(l1 - l2):
                p1 = p1.next
        else:
            for i in range(l2 - l1):
                p2 = p2.next

        while p1 and p2 and p1.val != p2.val:
            p1 = p1.next
            p2 = p2.next

        return p1

    def getLen(self, head):
        count = 0
        while head:
            count += 1
            head = head.next

        return count

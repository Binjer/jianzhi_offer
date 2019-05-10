# 合并两个递增排序的链表, 使得排序后的链表仍然是排序的

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        cur1 = pHead1
        cur2 = pHead2
        newHead = None

        # 注意等于号一定要考虑到, 一个逻辑里面处理就可以了.
        if cur1.val <= cur2.val:
            newHead = cur1
            newHead.next = self.Merge(cur1.next, cur2)
        elif cur1.val > cur2.val:
            newHead = cur2
            newHead.next = self.Merge(cur1, cur2.next)

        return newHead

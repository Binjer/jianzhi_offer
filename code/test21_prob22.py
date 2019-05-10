# 链表中的倒数第k个节点
# 要求: 只能遍历一遍链表

class Solution:
    def FindKthToTail(self, head, k):
        # write code here

        # 代码鲁棒性控制
        if k <= 0:
            return None

        p1 = head
        p2 = head
        for i in range(k):
            # 如果没有k个节点, 返回None
            if p1 is None:
                return None
            p1 = p1.next

        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        return p2

# 相关题目: 求链表的中间节点. 如果节点个数是偶数, 返回中间两个的任意一个.
# 思路: 定义两个指针, 一个指针一次走一步, 另一个指针一次走两步,
# 当走的快的指针走到尾部的时候, 走的慢的指针刚好在中间

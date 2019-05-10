# 链表中环的入口节点
# 思路分析:
# 首先确定链表中是否有环
# 有环之后怎么确定环的入口节点
# 知道了环中的节点数目, 就可以找到环的入口节点了

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here

        # 代码的鲁棒性
        if not pHead or pHead.next is None:
            return None

        p1 = pHead
        p2 = pHead

        # 先找有没有环
        while p1 is not None and p1.next is not None:
            p1 = p1.next.next
            p2 = p2.next

            if p1 == p2:
                break

        # 确定环里面有几个节点
        meetingNode = p1
        count = 1
        while p1.next != meetingNode:
            p1 = p1.next
            p2 = p2.next
            count += 1

        # 前面的指针先走节点的个数步, 然后两个指针同时以相同的速度走下去, 相遇的节点就是入口节点
        pre = pHead
        post = pHead
        for i in range(count):
            pre = pre.next

        while pre != post:
            pre = pre.next
            post = post.next

        return post

# 上述代码可以简化的, 确认有环后, 把一个节点重新指向头结点, 再以相同的速度往下走,相遇的节点就是环的入口节点

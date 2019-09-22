# 面试题23：链表中环的入口节点

# 思路分析:
# 首先确定链表中是否有环
# 有环之后怎么确定环的入口节点
# 知道了环中的节点数目, 就可以找到环的入口节点了


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 解法一：书中思路
class Solution1(object):
    def EntryNodeOfLoop(self, pHead):

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

        # 书上分步的思路
        # # 确定环里面有几个节点
        # meetingNode = p1
        # count = 1
        # while p1.next != meetingNode:
        #     p1 = p1.next
        #     p2 = p2.next
        #     count += 1
        #
        # # 前面的指针先走节点的个数步, 然后两个指针同时以相同的速度走下去, 相遇的节点就是入口节点
        # pre = pHead
        # post = pHead
        # for i in range(count):
        #     pre = pre.next
        #
        # while pre != post:
        #     pre = pre.next
        #     post = post.next
        #
        # return post

        # 上述代码可以简化的, 确认有环后, 把一个节点重新指向头结点, 再以相同的速度往下走,相遇的节点就是环的入口节点
        # 证明见：https://www.cnblogs.com/shiganquan/p/9340999.html
        p1 = pHead
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


# 解法二：断链法
class Solution2(object):
    def EntryNodeOfLoop(self, pHead):

        if pHead.next is None or pHead.next is None:
            return None

        newHead = ListNode(-1)
        newHead.next = pHead  # 用一个新节点记录完整的链表

        pre = newHead  # 链表第一个节点也可能是环的入口
        walkNode = pHead

        while walkNode is not None:
            pre.next = None
            pre = walkNode
            walkNode = walkNode.next

        return pre


# 解法三：利用哈希表
class Solution3(object):
    def EntryNodeOfLoop(self, pHead):

        if pHead.next is None or pHead.next is None:
            return None

        d = {}
        cur = pHead

        while cur is not None:
            if cur in d:
                return cur
            else:
                d[cur] = 1
            cur = cur.next

        return cur

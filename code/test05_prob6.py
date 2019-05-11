# 面试题6: 从尾到头打印链表
# 看能不能改变原链表, 不能的话就将原链表复制一份, 需要额外的空间. 之后用栈是最方便的
# 因此第一步: 将链表逆序; 第二步: 输出链表数据

# 这道题本质上考察的是如何实现一个单向链表的逆序, 一般来说有三种方法.
# 原地逆序, 递归法和插入法

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 下面是有头结点的情况的链表的三种逆序
# 方法一： 原地逆序
def reverse_linkedlist1(head):
    if head is None or head.next is None:
        return

    # 考虑有头结点的情况
    cur = head.next  # 指向第一个数据节点
    next = cur.next
    cur.next = None  # 把第一个数据节点变成最后一个数据节点

    pre = cur  # 第一个数据节点
    cur = next  # 第二个数据节点

    while cur.next is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    cur.next = pre
    head.next = cur


# 方法二 递归逆序
def reverse_linkedlist2(head):
    if head is None or head.next is None:
        return

    firstNode = head.next

    newhead = recursive_reverse(firstNode)

    # 头结点指向链表最后一个节点, 也即逆序后的第一个节点
    head.next = newhead
    return newhead


def recursive_reverse(head):
    if head is None or head.next is None:
        return head
    else:
        newhead = recursive_reverse(head.next)
        head.next.next = head
        head.next = None
    return newhead


# 方法三. 插入法
# 从第二个节点开始, 依次将其插入头结点和第一个节点之间
def reverse_linkedlist3(head):
    if head is None or head.next is None:
        return

    # 指向第二个数据节点
    cur = head.next.next
    # 设置第一个节点为尾节点
    head.next.next = None

    while cur is not None:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next


if __name__ == '__main__':
    head = Node(0)

    cur1 = head
    i = 1
    while i < 8:
        tmp = Node(i)
        cur1.next = tmp
        cur1 = tmp
        i += 1

    cur2 = head.next
    while cur2 is not None:
        print(cur2.val, end=" ")
        cur2 = cur2.next
    print()

    reverse_linkedlist3(head)
    cur3 = head.next
    while cur3 is not None:
        print(cur3.val, end=" ")
        cur3 = cur3.next


# 下面给出牛客网版本(没有头结点)
# 1.借助栈
class Solution1(object):
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []

        l = []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        l = list(reversed(l))
        return l


# 2.原地逆序
class Solution2(object):
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []

        pre = None
        cur = listNode
        while cur.next is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        cur.next = pre
        listNode = cur

        l = []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next

        return l


# 3.插入法
class Solution3(object):
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []

        pre = listNode
        cur = listNode.next
        listNode.next = None
        while cur is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        listNode = pre

        s = []
        while listNode:
            s.append(listNode.val)
            listNode = listNode.next

        return s


# 4.递归法
class Solution4(object):
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []

        listNode = self.recursiveCore(listNode)

        s = []
        while listNode:
            s.append(listNode.val)
            listNode = listNode.next

        return s

    def recursiveCore(self, head):
        if not head or not head.next:
            return head

        newHead = self.recursiveCore(head.next)
        head.next.next = head
        head.next = None

        return newHead

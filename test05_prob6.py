# 从尾到头打印链表
# 看能不能改变原链表, 不能的话就将原链表复制一份, 需要额外的空间. 用栈是最方便的
# 因此第一步: 将链表逆序; 第二步: 输出链表数据

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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


# 3. 插入法
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

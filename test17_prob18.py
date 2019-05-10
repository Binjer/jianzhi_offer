class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_node(self, head, delNode):
        """
        删除指定节点
        """
        # 这里假设链表是有头结点的, 并且删除的链表结点也有可能是头结点.

        if not (head and delNode):
            return False

        # 要删除的节点不是尾节点
        # 假如要删除的是头结点, 原来的头结点是没有数据的, 直接把它后一个节点的数据复制给它, 链表的结构就和之前不同了
        if delNode.next:
            next = delNode.next
            delNode.val = next.val
            delNode.next = next.next

            # 下面两句感觉没必要, 但是完成了资源回收的作用吧.
            next.val = None
            next.next = None


        # 注意, 这里默认有delNode.next is None的条件,
        # 所以这里表示的情况是只有链表只有一个节点
        elif head == delNode:
            head = None
        # 下面的else的默认条件是delNode.next is None and head != delNode:
        # 即要删除的节点是尾节点, 但是链表不止一个节点
        else:
            pre = None
            cur = head
            while cur.next is not None:
                pre = cur
                cur = cur.next
            pre.next = None


# 删除有序链表中重复的节点, 这里是重复的元素不保留的情况
class Solution2(object):
    def deleteDuplication(self, pHead):
        # write code here
        newHead = ListNode(-1)
        newHead.next = pHead

        pre = newHead
        cur = pHead

        while cur and cur.next:
            if cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return newHead.next


def linkedListGenerate(list):
    if len(list) == 0 or not list:
        return False

    head = ListNode(-1)
    cur = head
    while list:
        newNode = ListNode(list.pop(0))
        cur.next = newNode
        cur = newNode

    return head


# 创建一个链表
list = [1]
head = linkedListGenerate(list)
cur = head.next
while cur is not None:
    print(cur.val, end=" ")
    cur = cur.next
print("\t")


def middleNode(head):
    # if not head or head.next is None:
    #     return None

    fast = head
    slow = head

    if head is None:
        return False

    if head.next is None:
        return head

    while head is not None and head.next is not None:
        fast = fast.next
        slow = slow.next
        if fast.next is None:
            return slow
        fast = fast.next


print(middleNode(head).val)

# s = Solution2()
# newHead = s.deleteDuplication(head)
# first = newHead.next
#
# while first is not None:
#     print(first.val)
#     first = first.next

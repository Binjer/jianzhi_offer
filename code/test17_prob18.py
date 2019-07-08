# 面试题18：删除链表的节点


# 节点类定义如下
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 题目一：在0(1)时间内删除链表节点
# 下面解法的平均时间复杂度是[(n-1)xO(1) + O(n)]/n = O(1)
class Solution(object):
    def delete_node(self, head, delNode):
        """
        删除指定节点
        """
        # 这里假设链表是有头结点的, 并且删除的链表结点也有可能是头结点.
        if not (head and delNode):
            return False

        # 直接用要删除节点的后一个节点的值覆盖它的值，再把它的next指向下下一个节点(不用顺序查找所以是0(1)的时间复杂度)
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
        # 即要删除的节点是尾节点, 但是链表不止一个节点, 这时只能顺序查找到倒数第二个节点了
        else:
            pre = None
            cur = head
            while cur.next is not None:
                pre = cur
                cur = cur.next
            pre.next = None


# 题目2：删除有序链表中重复的节点, 这里是重复的元素不保留的情况
class Solution2(object):
    def deleteDuplication(self, pHead):

        # 建一个新节点，因为可能头节点会被删除
        newHead = ListNode(-1)
        newHead.next = pHead

        pre = newHead
        cur = pHead

        while cur and cur.next:
            if cur.val == cur.next.val:
                val = cur.val
                # 找到下一个不重复的节点(值与val不同)
                while cur and cur.val == val:  # 当找到链表尾部时, cur=None才会结束
                    cur = cur.next
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next

        return newHead.next


# 下面是测试所用的代码
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
# list = [1, 2, 3, 4, 5, 6, 7]
list = [1, 2, 3, 3, 4, 4, 5]

head = linkedListGenerate(list)
cur = head.next

# 打印链表
while cur is not None:
    print(cur.val, end=" ")
    cur = cur.next
print("\t")


# # 找到链表中间的节点
# def middleNode(head):
#     # if not head or head.next is None:
#     #     return None
#
#     fast = head
#     slow = head
#
#     if head is None:
#         return False
#
#     if head.next is None:
#         return head
#
#     while head is not None and head.next is not None:
#         fast = fast.next
#         slow = slow.next
#         if fast.next is None:
#             return slow
#         fast = fast.next
#
#
# print(middleNode(head).val)

s = Solution2()
newHead = s.deleteDuplication(head)
first = newHead.next

while first is not None:
    print(first.val, end=" ")
    first = first.next

# 面试题9: 用两个栈实现队列

# 解题思路:
# 对于栈1和栈2, 每次插入新元素时,都先push到栈1;
# 每次弹出元素时, 先看栈2是否为空, 不为空的话就直接弹出栈2的顶部元素, 就是最先进入队列的那个;
# 如果栈2为空, 栈1也为空, 那么返回None;
# 如果栈2为空, 栈一不为空, 先把栈1中的元素依次弹出并压入栈2中, 然后弹出栈2的栈顶元素


class Solution(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):

        self.stack1.append(node)

    def pop(self):

        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


# 题目变形: 两个队列模拟一个栈
# 解题思路:
# 插入元素时还是只插入某一个队列;
# 删除某一个元素时, 因为栈是先入先出, 我们只能在队列头部删除元素, 因此把队列元素依次删除并加入到另一个队列中;
# 然后交换这两个队列的作用, 并弹出第一个(交换后变成第二个队列中)仅剩的一个元素


class Solution2(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, node):

        self.queue1.insert(0, node)

    def pop(self):

        if not self.queue1:
            return None

        while len(self.queue1) != 1:
            self.queue2.insert(0, self.queue1.pop())
        # 要保证元素多的那个队列始终为第一个队列
        self.queue1, self.queue2 = self.queue2, self.queue1

        return self.queue2.pop()


# if __name__ == '__main__':
#     a = Solution2()
#     a.push(1)
#     a.push(7)
#     a.push(3)
#     a.push(5)
#     print(a.pop())
#     print(a.pop())
#     print(a.pop())
#     print(a.pop())
#     print(a.pop())

# 圆圈中最后剩下的数字
# 约瑟夫问题

# 解法一:
# 使用双端队列, 把一个数从右边弹出再从左边加入, 直到数到要求的数, 弹出右边的数
# 直到队列中只剩下最后一个数
from collections import deque


# 算法时间复杂度为O(mn), 空间复杂度为O(n)
class Solution1(object):
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1

        q = deque()

        for i in range(n):
            q.appendleft(i)

        while len(q) > 1:
            for i in range(m - 1):
                q.appendleft(q.pop())
            q.pop()

        return q[0]


# s = Solution1()
# print(s.LastRemaining_Solution(5, 3))


# 用列表的话会当n很大时, 效率很低
# class Solution2:
#     def LastRemaining_Solution(self, n, m):
#         # write code here
#         if n < 1 or m < 1:
#             return -1
#         q = []
#         for i in range(n):
#             q.insert(0, i)
#
#         while len(q) > 1:
#             for i in range(m - 1):
#                 q.insert(0, q.pop())
#             q.pop()
#
#         return q[0]


# 数学规律
# 基于循环的实现
# 算法时间复杂度为O(n), 空间复杂度为O(1)
class Solution21(object):
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1

        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i

        return last


# 递归同样不适用于n特别大的情况
class Solution22:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        if n == 1:
            return 0
        else:
            return (self.LastRemaining_Solution(n - 1, m) + m) % n


def comp(m, n):
    a = m % n
    b = m % n % n

    if a == b:
        return True


s = True
for i in range(1, 1000):
    for j in range(1000, 0, -1):
        s = s & comp(i, j)

print(s)

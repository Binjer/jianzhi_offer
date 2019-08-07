# 面试题59：滑动窗口中的最大值

#

# 解法一: 暴力解法O(nk)
class Solution1(object):
    def maxInWindows(self, num, size):

        if not num or size <= 0:
            return []

        res = []
        for i in range(len(num) - size + 1):
            res.append(max(num[i:i + size]))

        return res


# 解法二: 利用双端队列
class Solution2(object):
    def maxInWindows(self, num, size):

        if not num or size <= 0:
            return []

        res = []
        if (len(num) >= size) and (size >= 1):
            deque = []

            # 这是先找到第一个窗口里面的最大值.
            for i in range(size):
                while deque and num[i] >= num[deque[-1]]:
                    deque.pop()
                deque.append(i)

            for i in range(size, len(num)):
                res.append(num[deque[0]])

                while deque and num[i] >= num[deque[-1]]:
                    deque.pop()

                if deque and i - deque[0] >= size:
                    deque.pop(0)
                deque.append(i)

            res.append(num[deque[0]])

        return res


s = Solution2()
print(s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3))


# 引申题目：队列的最大值
# 定义一个队列并实现max得到队列里的最大值，要求函数max, push_back, pop_front的时间复杂度都是O(1)
# 和面试题30：包含min函数的栈类似，都是维护两个容器，一个保存数据，一个保存当前最大(小)值
class Queue(object):

    def __init__(self):
        self.data = []
        self.max_data = []

    def pop(self):
        """
        pop out the head element
        :return: head element
        """
        if not self.data:
            raise Exception('Empty Queue Cannot Pop')

        if self.data[0] == self.max_data[0]:
            self.max_data.pop(0)

        return self.data.pop(0)

    def push(self, x):
        """
        push in the back
        :param x: element
        :return: None
        """
        self.data.append(x)
        while self.max_data and self.max_data[-1] < x:
            self.max_data.pop()
        self.max_data.append(x)

        return

    def max(self):
        """
        get the maximum element
        :return: max element
        """
        return self.max_data[0]


q = Queue()
q.push(5)
q.push(6)
q.pop()
print(q.max())

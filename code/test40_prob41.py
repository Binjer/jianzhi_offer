# 数据流中的中位数

# 1.使用排序的数组
# 插入元素: O(n) 查找中位数: O(1)
class Solution:
    def __init__(self):
        self.li = []

    def Insert(self, num):
        # write code here
        self.li.append(num)
        self.li.sort()

    def GetMedian(self, M):
        # write code here
        length = len(self.li)
        if length == 0:
            return []
        if length % 2 == 1:
            return self.li[length // 2]
        else:
            return (self.li[length / 2 - 1] + self.li[length / 2]) / 2.0


# import heapq
# 堆排序的实现
# def heapsort(iterable):
#     h = []
#     for value in iterable:
#         heapq.heappush(h, value)
#
#     return [heapq.heappop(h) for i in range(len(h))]
#
#
# print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# 维护一个最大堆和一个最小堆

class Solution2:
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def Insert(self, num):
        import heapq
        # 总数为奇数插入最大堆
        if (len(self.maxheap) + len(self.minheap)) & 1:
            if len(self.minheap) > 0:
                if num > self.minheap[0]:
                    heapq.heappush(self.minheap, num)
                    heapq.heappush(self.maxheap, -self.minheap[0])
                    heapq.heappop(self.minheap)
                else:
                    heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.maxheap, -num)
        # 总数为偶数插入最小堆
        else:
            if len(self.maxheap) > 0:
                if num < -self.maxheap[0]:
                    heapq.heappush(self.maxheap, -num)
                    heapq.heappush(self.minheap, -self.maxheap[0])
                    heapq.heappop(self.maxheap)
                else:
                    heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.minheap, num)

    def GetMedian(self, n=None):
        if (len(self.maxheap) + len(self.minheap)) & 1:
            mid = self.minheap[0]
        else:
            mid = (self.minheap[0] - self.maxheap[0]) / 2.0
        return mid

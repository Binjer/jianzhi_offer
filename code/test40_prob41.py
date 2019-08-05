# 面试题41：数据流中的中位数

# 1.使用排序的数组
# 插入元素: O(n). 插入新数据时让数组保持有序，可能需要移动n个数，所以时间复杂度为O(n)
# 查找中位数: O(1)


class Solution(object):
    def __init__(self):
        self.li = []

    def Insert(self, num):

        self.li.append(num)
        self.li.sort()

    def GetMedian(self, M):

        length = len(self.li)
        if length == 0:
            return []
        if length % 2 == 1:
            return self.li[length // 2]
        else:
            return (self.li[length // 2 - 1] + self.li[length // 2]) / 2.0


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

# 方法二：维护一个最大堆和一个最小堆
# 中位数左边的数放在一个最大堆容器里，右边的数放在一个最小堆容器里，同时保证最小堆里的数都比最大堆里的数大
# 插入的时间复杂度：O(logn); 得到中位数的时间复杂度：O(1)
class Solution2(object):
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def Insert(self, num):
        import heapq
        # 总数为奇数插入最大堆
        if (len(self.maxheap) + len(self.minheap)) & 1:
            # 如果最小堆不为空
            if len(self.minheap) > 0:
                # 如果待插入的元素比最小堆的最小值大，则先把该元素插入到最小堆中，再把最小堆中的最小值插入到最大堆中，再从最小堆中弹出最小值
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
                # 如果待插入的元素比最大堆的最大值小，则先把该元素插入到最大堆中，再把最大堆中的最大值插入到最小堆中，再从最大堆中弹出最大值
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

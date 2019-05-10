# 最小的k个数
# 输入n个整数, 找出其中最小的k个数.
# 问题分析: 对时间和空间的要求, 是否是海量数据情形

class Solution1:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        # 这里需要多判断一下数组为空的情况
        if k > len(tinput) or len(tinput) <= 0:
            return []

        res = self.partitionOfK(tinput, 0, len(tinput) - 1, k)
        return res

    def partitionOfK(self, numbers, start, end, k):
        # if k < 0 or numbers == [] or start < 0 or end >= len(numbers) or k > end:
        #     return None
        low = start
        high = end
        key = numbers[start]
        while low < high:
            while low < high and numbers[high] > key:
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low] <= key:
                low += 1
            numbers[high] = numbers[low]
        # 找到了基准元素的位置
        numbers[low] = key

        if low < k:
            # 这里需要处理一下输出整个数组的情况
            # 因为快速排序的话如果右边只有一个数字的话就不会再排序了
            if low == len(numbers) - 1:
                return numbers[:]
            return self.partitionOfK(numbers, low + 1, end, k)
        elif low > k:
            return self.partitionOfK(numbers, start, low - 1, k)
        else:
            return numbers[:low]


# s = Solution1()
# input1 = [4, 5, 1, 6, 2, 7, 3, 8]
# print(s.GetLeastNumbers_Solution(input1, 8))


# 适用于海量数据情况
# 1.创建一个大小为k的容器
# 2.从数组中依次读入一个数,当容器未满时, 直接加入;
#  容器已满时, 将新数据与容器中的最大值比较,比最大值小则替换,否则不变



class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        import heapq
        if k > len(tinput):
            return []

        return heapq.nsmallest(k, tinput)





# 面试题39：数组中出现次数超过一半的数字


# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

# 先排序, 然后遍历比较某个位置的值和索引比它多出n/2的位置的值是否相等.
# 排序nlogn, 最差的情况还需要遍历n/2, 总复杂度是n*logn + n/2
class Solution1(object):
    def MoreThanHalfNum_Solution(self, numbers):

        if not numbers or len(numbers) <= 0:
            return 0

        numbers = sorted(numbers)
        dis = len(numbers) // 2
        for i in range(len(numbers)):
            if i + dis < len(numbers) and numbers[i] == numbers[i + dis]:
                return numbers[i]
        return 0


# num1 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
# s = Solution1()
# res = s.MoreThanHalfNum_Solution(num1)
# print(res)


# 第二种解法: 在任意数组中查找第k大的数的O(n)算法, 基于快排的思想
# 因为如果一个数字出现次数超过了数组的一半， 那么排序后位于数组中间的数字一定就是这个数字。
# 即要找到长度为n的数组中第n/2大的数字，也就是统计学上的中位数。
# 最后，找出中位数后要检查中位数出现的次数是否满足要求
class Solution2(object):
    def MoreThanHalfNum_Solution(self, numbers):

        if not numbers or len(numbers) <= 0:
            return 0

        res = self.partitionOfK(numbers, 0, len(numbers) - 1, len(numbers) // 2)

        if self.CheckMoreThanHalfNum(numbers, res):
            return res
        return 0

    def partitionOfK(self, numbers, start, end, k):

        # 这两行代码保证了代码的鲁棒性, 一定不要忘了加上
        # if k < 0 or numbers == [] or start < 0 or end >= len(numbers) or k > end:
        #     return None

        low = start
        high = end
        key = numbers[start]
        while low < high:
            while low < high and numbers[high] >= key:
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low] <= key:
                low += 1
            numbers[high] = numbers[low]
        # 找到了基准元素的位置
        numbers[low] = key

        if low < k:
            return self.partitionOfK(numbers, low + 1, end, k)
        elif low > k:
            return self.partitionOfK(numbers, start, low - 1, k)
        else:
            return numbers[low]

    def CheckMoreThanHalfNum(self, numbers, res):
        count = 0
        for i in range(len(numbers)):
            if numbers[i] == res:
                count += 1
        if count * 2 <= len(numbers):
            return 0
        return 1


# numbers = [3, 5, 6, 7, 2, -1, 9, 3]
# print(sorted(numbers))
# print(partitionOfK(numbers, 0, len(numbers) - 1, 6))


# 解法三:
# 不修改原来的数组
# 遍历数组的时候保存两个值，一个表示数组中的第一个数字，一个表示出现的次数；
# 如果下一个数字和我们之前保存的数字相同，那么次数加1l; 如果下一个数字和我们之前保存的数字不同，次数减1；
# 如果次数为0，那我们需要保存下一个数字，并把次数设为1，最后一个把次数设为1对应的数字一定是那个出现次数超过数组一般长度的数字
class Solution3(object):
    def MoreThanHalfNum_Solution(self, numbers):

        if not numbers or len(numbers) <= 0:
            return 0

        res = numbers[0]
        count = 1
        for i in range(1, len(numbers)):
            if count == 0:
                res = numbers[i]
                count = 1
            elif numbers[i] == res:
                count += 1
            else:
                count -= 1
        print(count)

        if self.CheckMoreThanHalfNum(numbers, res):
            return res

        return 0

    def CheckMoreThanHalfNum(self, numbers, res):
        count = 0
        for i in range(len(numbers)):
            if numbers[i] == res:
                count += 1
        if count * 2 <= len(numbers):
            return 0
        return 1


s = Solution3()
print(s.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))

# # 补充: 快速排序
# def quick_sort(li, start, end):
#     if start >= end:
#         return
#
#     low = start
#     high = end
#
#     pivot = li[start]
#
#     while low < high:
#         # 先从右边找比基准元素小的数
#         while low < high and li[high] >= pivot:
#             high -= 1
#         li[low] = li[high]
#
#         # 再从左边找比基准元素大的数
#         while low < high and li[low] < pivot:
#             low += 1
#         li[high] = li[low]
#
#     li[low] = pivot  # 基准元素的位置就确定了，此时它左边的数都比它小，右边的数都比它大
#
#     quick_sort(li, start, low - 1)
#     quick_sort(li, low + 1, end)
#
#
# li = [3, 2, 1, 10, 1, 6, 9, 4]
# quick_sort(li, 0, len(li) - 1)
# print(li)

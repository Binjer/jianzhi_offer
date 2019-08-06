# 面试题54：在排序数组中查找给定数字出现的次数

# 给定一个排序的数组和一个数，统计这个数在数组中出现的次数

# 最直观的解法是遍历一遍整个数组，每次遇到指定数字，则次数加一
# 这种思路显然没有用到排序数组的性质


# 更高效的解法：二分查找
# 先找到数字出现的第一个位置, 同理找到数字出现的最后一个位置
# 算法时间复杂度是logn
class Solution(object):
    def getNumberOfK(self, nums, k):

        if not nums or len(nums) <= 0:
            return 0

        first = self.getFirstK(nums, k, 0, len(nums) - 1)
        last = self.getLastK(nums, k, 0, len(nums) - 1)

        res = 0
        if first > -1 and last > -1:
            res = last - first + 1
        return res

    def getFirstK(self, nums, k, start, end):

        if start > end:
            return -1

        middleIndex = (start + end) // 2
        middleData = nums[middleIndex]

        if middleData == k:
            if middleIndex > 0 and nums[middleIndex - 1] != k or middleIndex == 0:
                return middleIndex
            else:
                end = middleIndex - 1

        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1

        return self.getFirstK(nums, k, start, end)

    def getLastK(self, nums, k, start, end):

        if start > end:
            return -1

        middleIndex = (start + end) // 2
        middleData = nums[middleIndex]

        if middleData == k:
            if middleIndex < len(nums) - 1 and nums[middleIndex + 1] != k or middleIndex == len(nums) - 1:
                return middleIndex
            else:
                start = middleIndex + 1
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1

        return self.getLastK(nums, k, start, end)


# 题目变形: 0~n-1中缺失的数字
class Solution11(object):
    def getMissingNumber(self, nums):

        if not nums or len(nums) <= 0:
            return 0

        # 无效的输入, 比如数组不是按要求排序的
        # 下面是数字不在0~n-1范围内. 此外还要考虑是否有重复数字出现等不满足情况的输入等
        for i in nums:
            if i > len(nums):
                return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] != middle:
                if middle == 0 or nums[middle - 1] == middle - 1:
                    return middle
                else:
                    right = middle - 1

            else:
                left = middle + 1

        if left == len(nums):
            return left


# 题目变形2:
# 假设一个单调递增的数组里的每个元素都是整数并且是唯一的。
# 请编程实现一个函数找出数组中任意一个数值等于其下标的元素。
class Solution22(object):
    def getNumberSameAsIndex(self, nums):

        if not nums or len(nums) <= 0:
            return 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) >> 1
            if nums[middle] == middle:
                return middle
            elif nums[middle] > middle:
                right = middle - 1
            else:
                left = middle + 1

        return -1

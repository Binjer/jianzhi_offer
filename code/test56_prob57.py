# 和为s的数字

# 很容易想到O(n2)的解法
class Solution1(object):
    def findNumbersWithSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [nums[i], nums[j]]

        return -1


# 利用哈希表, 以空间换时间
# O(n)的时间复杂度, O(n)的空间复杂度
class Solution(object):
    def findNumbersWithSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = {}
        for i in nums:
            l[target - i] = 1

        for j in l:
            if j in nums:
                return [target - j, j]

        return -1


# 如果要求时间复杂度为O(n), 空间复杂度为O(1)呢?
# 利用题目中提供的额外信息, 即数组是排序的
# 用两个指针,一个指向第一个数字, 一个指向最后一个数字
class Solution3:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        nums = array
        target = tsum

        if not nums or len(nums) <= 0:
            return []

        pre = 0
        post = len(nums) - 1

        while pre < post:
            curNum = nums[pre] + nums[post]

            if curNum == target:
                return [nums[pre], nums[post]]
            elif curNum > target:
                post -= 1
            else:
                pre += 1

        return []


# 题目进阶: 和为s的连续正数序列
# 从上面维护两个指针的思路得到启发
class Solution21:
    def FindContinuousSequence(self, tsum):
        # write code here

        if not tsum or tsum <= 0:
            return -1

        res = []
        small = 1
        big = 2
        curSum = small + big
        middle = (1 + tsum) / 2

        while small < middle:
            if curSum == tsum:
                res.append(range(small, big + 1))
                big += 1
                curSum += big
            elif curSum < tsum:
                big += 1
                curSum += big
            else:
                curSum -= small
                small += 1

        return res

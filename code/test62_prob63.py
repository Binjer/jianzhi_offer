# 股票的最大利润

# 解法一: 暴力解法, 找到所有数对差值的最大值
# O(n2)的时间复杂度 的时间复杂度
class Solution(object):
    def maxDiff(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) <= 1:
            return 0

        curMax = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] - nums[i] > curMax:
                    curMax = nums[j] - nums[i]

        return curMax


# 解法二
# 用一个值记录前n-1个数字的最小值, 同时也记录遍历到当前数字时的最大价值
class Solution2(object):
    def maxDiff(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) <= 1:
            return 0

        minprice = nums[0]
        maxvalue = nums[1] - minprice

        for i in range(2, len(nums)):
            if nums[i - 1] < minprice:
                minprice = nums[i - 1]

            if nums[i] - minprice > maxvalue:
                maxvalue = nums[i] - minprice

        # 处理价值为负的情况, 要视题目要求而定
        if maxvalue < 0:
            return 0

        return maxvalue

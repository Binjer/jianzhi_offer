# 面试题57：和为s的数字

# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
# 如果有多对数字的和等于s，则输出任意一对即可。


# 很容易想到O(n2)的解法
class Solution1(object):
    def findNumbersWithSum(self, array, tsum):
        """
        :type array: List[int]
        :type tsum: int
        :rtype: List[int]
        """

        # 异常输入处理
        if not array or len(array) <= 0:
            return []

        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == tsum:
                    return [array[i], array[j]]

        return []


# 利用哈希表, 以空间换时间
# O(n)的时间复杂度, O(n)的空间复杂度
# 这种方法也没有利用数组已经排序的性质
class Solution(object):
    def findNumbersWithSum(self, array, tsum):
        """
        :type array: List[int]
        :type tsum: int
        :rtype: List[int]
        """

        # 异常输入处理
        if not array or len(array) <= 0:
            return []

        l = {}
        for i in array:
            l[tsum - i] = i

        for j in array:
            if j in l:
                return [j, l[j]]

        return []


# 如果要求时间复杂度为O(n), 空间复杂度为O(1)呢?
# 利用题目中提供的额外信息, 即数组是排序的
# 用两个指针,一个指向第一个数字, 一个指向最后一个数字
class Solution3(object):
    def FindNumbersWithSum(self, array, tsum):

        if not array or len(array) <= 0:
            return []

        p1 = 0  # 指向数组中最小的数
        p2 = len(array) - 1  # 指向数组中最大的数

        while p1 < p2:
            if array[p1] + array[p2] == tsum:
                return [array[p1], array[p2]]
            elif array[p1] + array[p2] > tsum:
                p2 -= 1
            else:
                p1 += 1

        return []


# 题目进阶: 和为s的连续正数序列
# 从上面维护两个指针的思路得到启发
class Solution21:
    def FindContinuousSequence(self, tsum):

        if not tsum or tsum <= 2:
            return []

        small = 1
        big = 2
        curSum = small + big
        res = []

        while small < (1 + tsum) // 2:
            if curSum == tsum:
                res.append(range(small, big + 1))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big

        return res

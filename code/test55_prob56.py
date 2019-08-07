# 面试题56：数组中只出现一次的两个数字

# 一个整型数组里除了两个数字之外，其他的数字都出现了两次，请找出这两个只出现一次的数字
# 如果要求只使用 O(n) 的时间和额外 O(1) 的空间，该怎么做呢

# 如果只有一个数字只出现一次，其它数字都出现两次，那么我们可以从头到尾异或数组中的每个数字，那么最终的结果一定是那个只出现一次的数字
# 此时有两个不一样的数字，我们还是从头到尾异或数组中的每一个数字，最后的结果应该是要找的两个数字的异或结果，应该为1
# 这个结果二进制表示中一定有一位为1，两个只出现一次的数字在这一位上肯定不同，我们按照二进制中这一位是不是1将原数组分为两个子数组
# 出现了两次的数字肯定会被分到同一个数组中去


class Solution1(object):
    def findNumsAppearOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums or len(nums) <= 0:
            return

        res = 0
        for i in nums:
            res = res ^ i

        index = self.findFirstBit(res)

        res1 = 0
        res2 = 0

        for j in nums:
            # 根据对应位置是否为1将数组分成两部分,
            # 相同的两个数一定会被分到同一组, 因为它们每一位都相同
            # 不同的两个数就被分到两个数组里面了. 对每个数组分别求所有元素的异或就可以找到只出现一次的数字了
            if j >> index & 1 == 1:
                res1 = res1 ^ j
            else:
                res2 = res2 ^ j

        return [res1, res2]

    def findFirstBit(self, num):
        '''
        找到异或结果从右往左(低位到高位)第一个为1的位置
        :param num:
        :return:
        '''
        indexBit = 0
        while num & 1 == 0 and indexBit < 32:
            num >>= 1
            indexBit += 1

        return indexBit


# 题目二:
# 数组中唯一只出现一次的数字
# 在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。

# 先排序再找: O(nlogn + n)的时间复杂度;  哈希表: O(n)的时间复杂度, O(n)的空间复杂度
# 如果要求只使用 O(n) 的时间和额外 O(1) 的空间，该怎么做呢
class Solution22(object):
    def findNumberAppearingOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) <= 0:
            return -1

        res = [0] * 32

        for i in range(len(nums)):
            # 对nums中的每一个元素的32位二进制表示对应相加存到res中
            bitIndex = 1
            for j in range(31, -1, -1):
                tmp = nums[i] & bitIndex
                if tmp != 0:
                    res[j] += 1

                bitIndex = bitIndex << 1

        # 技巧性方法
        result = 0
        for i in range(32):
            result = result << 1
            result += res[i] % 3

        # 直观方法, res中存放着最终结果的32位二进制表示, 从高位到低位
        # for i in range(len(res)):
        #     if res[i] % 3 == 0:
        #         res[i] = 0
        #     else:
        #         res[i] = 1
        #
        # res = res[::-1]
        # result = 0
        # for index, num in enumerate(res):
        #     result = result + (num * (2 ** index))

        return result


s = Solution22()
print(s.findNumberAppearingOnce([1, 2, 2, 2, 1, 1, 3, 4, 4, 4, 5, 5, 5]))




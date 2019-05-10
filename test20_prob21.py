# 调整一个数组中数字的顺序, 使得奇数位于偶数之前.
# 剑指offer里面没有要求奇偶数的相对位置不改变
# 奇数和偶数之间的相对位置保持不变


# 0(n)的时间复杂度, 需要0(n)的辅助空间
# def reOrderArray(self, array):
#
#     if not array or len(array) == 0:
#         return array
#
#     even = [i for i in array if i % 2 == 0]
#     odd = [i for i in array if i % 2 != 0]
#
#     array = odd + even
#
#     return array


class Solution:

    def reOrderArray(self, array):

        if not array or len(array) == 0:
            return array

        left = 0
        right = len(array) - 1

        # 维护前后两个指针这种思想很常用
        # 外部判断条件是left < right
        # 内部会分成三种情况
        while left < right:
            while left < right and not self.isEven(array[left]):
                left += 1
            while left < right and self.isEven(array[right]):
                right -= 1

            if left < right:
                array[left], array[right] = array[right], array[left]

        return array

    def isEven(self, x):

        return x % 2 == 0

# 面试题51：数组中的逆序对

# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字构成一个逆序对。
# 输入一个数组，求出这个数组中逆序对的总数

# 解法一：最容易想到的思路,
# 两层for循环, O(n2)的时间复杂度
class Solution1(object):
    def inversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 0:
            return 0

        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    count += 1

        return count


# 解法二: 类似归并排序
# 先把数组分割成子数组, 统计子数组之间的逆序对的树木;
# 再统计相邻子数组之间的逆序对的数目. 在统计的过程中, 对数组进行排序, 即生成了一个辅助数组.
class Solution2(object):
    def inversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 0:
            return 0

        length = len(nums)

        # copy = []
        # for i in range(length):
        #     copy.append(nums[i])
        copy = [i for i in nums]  # 等价于上面三行代码

        count = self.inverseCore(nums, copy, 0, length - 1)

        return count

    def inverseCore(self, nums, copy, start, end):

        if start == end:
            copy[start] = nums[start]
            return 0

        length = (end - start) // 2

        left = self.inverseCore(copy, nums, start, start + length)
        right = self.inverseCore(copy, nums, start + length + 1, end)

        i = start + length
        j = end

        indexCopy = end
        count = 0

        while i >= start and j >= start + length + 1:
            if nums[i] > nums[j]:
                copy[indexCopy] = nums[i]
                count += j - start - length  # 如果左边的数大于右边，那么有右边指针指向的索引个逆序对(右边指针指向右边最大的数)
                # count += j - (start - length + 1) + 1
                i -= 1
                indexCopy -= 1
            else:
                copy[indexCopy] = nums[j]
                j -= 1
                indexCopy -= 1

        while i >= start:
            copy[indexCopy] = nums[i]
            indexCopy -= 1
            i -= 1

        while j >= start + length + 1:
            copy[indexCopy] = nums[j]
            indexCopy -= 1
            j -= 1

        return left + right + count


# 解法三
# 先把数组复制一遍然后排序
# 然后统计新数组里面每一个元素在原来数组中的索引即可, 每统计一次需要在原数组中删除统计过的元素
# 时间复杂度来自于排序O(nlogn), list中根据值找到索引的时间复杂度是O(1)
class Solution3(object):
    def inversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 0:
            return 0

        count = 0
        copy = []
        for i in range(len(nums)):
            copy.append(nums[i])

        copy.sort()

        i = 0
        while len(copy) > i:
            count += nums.index(copy[i])  # 时间复杂度为O(1)
            nums.remove(copy[i])
            i += 1
        return count

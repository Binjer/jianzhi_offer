# 面试题3：找出数组中重复的数字


# 原始题目解法
class Solution1(object):
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):

        # 前面这两个判断是很重要的,保证了代码的鲁棒性
        # 当实现了函数的功能之后，要根据实际需求对各种异常情况进行处理
        if numbers is None or len(numbers) <= 1:
            return False
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return False

        # 方法一: 先排序, 然后遍历. 时间复杂度是O(nlogn+k)
        # numbers.sort()
        # for i in range(len(numbers) - 1):
        #     if numbers[i] == numbers[i + 1]:
        #         duplication[0] = numbers[i]
        #         return True
        # return False

        # 方法二: 利用哈希表: 时间复杂度是O(n), 空间复杂度是O(n)
        # used_dic = {}
        # used_dic = set()
        # for i in range(len(numbers)):
        #     if numbers[i] not in used_dic:
        #         used_dic[numbers[i]] = 1
        #     else:
        #         duplication[0] = numbers[i]
        #         return True

        # 方法三: 分析题干发现如果不存在重复的数字, 那么数组满足numbers[i] = i...
        # 每个数字最多只需要交换两次就能找到自己的位置O(2n)
        # 时间复杂度是O(n), 空间复杂度是O(1)
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    temp = numbers[i]
                    numbers[i] = numbers[temp]
                    numbers[temp] = temp

        return False


# 题目变形： 增加了额外的要求
# 不修改数组找出重复的数字
# 方法一: 和题目1中方法三同理
class Solution2:
    def duplicate1(self, numbers, duplication):

        if len(numbers) <= 0 or not numbers:
            return

        usedHashset = set()
        for i in range(len(numbers)):
            if numbers[i] not in usedHashset:
                usedHashset.add(numbers[i])
            else:
                duplication.insert(0, numbers[i])
                return True

    # 方法二
    # 先用m把数组分成两个部分, 如果没有重复的数字, 那么大于m的数字和小于m的数字数目
    # 思路类似于二分查找, 边查找边统计每部分的数量
    # 注意是对数进行二分查找, 不是索引
    # 对长度为n的数组需要查找logn次, 总的时间复杂度是nlogn
    # 书上思路代码
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        if len(nums) <= 0 or not numbers:
            return

        length = len(nums)
        start = 1
        end = length - 1

        while end >= start:
            middle = start + (end - start) / 2
            count = self.countNum(nums, length, start, middle)
            if end == start:
                if count > 1:
                    return start
                else:
                    break

            if count > (middle - start) + 1:
                end = middle
            else:
                start = middle + 1

        return False

    def countNum(self, numbers, length, start, end):
        count = 0
        for i in range(length):
            if numbers[i] < 1 or numbers[i] > length:
                return False
            if start <= numbers[i] <= end:
                count += 1
        return count

    # 更简洁的写法
    # 下面的代码是要求数组中必须存在重复的数字
    # [0,1,2,3]这种情况就处理不了了
    def duplicateInArray2(self, nums):

        if not nums or len(nums) <= 0:
            return

        l = 1
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l + 1) // 2
            count = 0
            for num in nums:
                if num < mid:
                    count += 1

            if count < mid:
                # 此时重复的数一定在 [mid,right] 中
                l = mid
            else:
                assert count >= mid
                r = mid - 1

        return l



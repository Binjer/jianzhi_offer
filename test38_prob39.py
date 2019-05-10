# 数组中出现次数超过一半的数字

# 先排序, 然后遍历比较某个位置的值和索引比它多出n/2的位置的值是否相等.
# 排序nlogn, 最差的情况还需要遍历n/2, 总复杂度是n*logn + n/2
class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
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
# 用这种算法的话找出中位数后要检查中位数出现的次数是否满足要求
class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
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
class Solution3:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers or len(numbers) <= 0:
            return 0

        res = numbers[0]
        count = 1
        for i in range(len(numbers)):
            if count == 0:
                res = numbers[i]
                count = 1
            elif numbers[i] == res:
                count += 1
            else:
                count -= 1

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

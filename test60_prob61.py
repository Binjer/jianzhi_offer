# 扑克牌中的顺子


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) <= 0:
            return False

        # 排序
        numbers.sort()

        # 统计0的个数
        countZero = 0
        for i in numbers:
            if i == 0:
                countZero += 1

        # 统计gap的个数, 看看0是不是能补全
        # 这里其实维护了两个指针, 一次遍历, 就可以计算出gap的值.
        # countGap = 0
        # small = countZero
        # big = small + 1
        # while big < len(numbers):
        #     if numbers[small] == numbers[big]:
        #         return False
        #
        #     countGap += numbers[big] - numbers[small] - 1
        #     small = big
        #     big += 1

        # 用for循环会更简单
        countGap = 0
        start = countZero
        for i in range(start, len(numbers) - 1):
            if numbers[i + 1] == numbers[i]:
                return False
            countGap += (numbers[i + 1] - numbers[i] - 1)

        return True if countZero >= countGap else False

# 面试题61：扑克牌中的顺子

# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2~10位数字本身，A为1，J为11，Q为12，K为13，大小王可以看成任意数字。这里用0表示


class Solution(object):
    def IsContinuous(self, numbers):

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
        # 统计非零元素之间的gap(为1时是连续的)
        for i in range(start, len(numbers) - 1):
            if numbers[i + 1] == numbers[i]:
                return False
            countGap += (numbers[i + 1] - numbers[i] - 1)

        return True if countZero >= countGap else False

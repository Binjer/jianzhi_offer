# 丑数

# 解法一
# 依次判断每一个数是不是丑数, 直到找够n个丑数为止
# 缺点: 效率很低.
class Solution1(object):
    def getUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while count < n:
            if self.isUglyCore(i):
                count += 1
                i += 1

        return i

    def isUglyCore(self, num):

        while num % 2 == 0:
            num /= 2

        while num % 3 == 0:
            num /= 3

        while num % 5 == 0:
            num /= 5

        return 1 if num == 1 else 0


# 解法二
# 以空间换时间, 将每次得到的丑数保存成一个数组, 后面的丑数由前面的计算而来
class Solution(object):
    def getUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 0:
            return 0

        uglyNum = [1]
        nextNum = 1
        nextIndex = 1

        p2 = p3 = p5 = 0

        while nextIndex < n:
            nextNum = min(uglyNum[p2] * 2, uglyNum[p3] * 3, uglyNum[p5] * 5)
            uglyNum.append(nextNum)

            while uglyNum[p2] * 2 <= nextNum:
                p2 += 1

            while uglyNum[p3] * 3 <= nextNum:
                p3 += 1

            while uglyNum[p5] * 5 <= nextNum:
                p5 += 1

            nextIndex += 1

        return nextNum

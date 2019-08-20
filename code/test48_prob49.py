# 面试题49：丑数

# 只包含因子2,3和5的数成为丑数，求按从小到大的熟悉怒的第1500个丑数。习惯上我们把1当作第一个丑数


# 解法一
# 依次判断每一个数是不是丑数, 直到找够n个丑数为止
# 缺点: 效率很低.
class Solution1(object):
    def GetUglyNumber_Solution(self, index):
        """
        :type index: int
        :rtype: int
        """

        if index == 0:
            return 1

        count = 0
        i = 0
        while count < index:
            i += 1
            if self.isUglyCore(i):
                count += 1

        return i

    def isUglyCore(self, num):

        while num % 2 == 0:
            num /= 2

        while num % 3 == 0:
            num /= 3

        while num % 5 == 0:
            num /= 5

        return 1 if num == 1 else 0


s1 = Solution1()
print(s1.GetUglyNumber_Solution(10))
# print(s1.GetUglyNumber_Solution(1500))  # 运行时间会非常久


# 解法二
# 以空间换时间, 将每次得到的丑数保存成一个数组, 后面的丑数由前面的计算而来
class Solution2(object):
    def GetUglyNumber_Solution(self, index):
        """
        :type index: int
        :rtype: int
        """

        if index <= 0:
            return 0

        uglyNum = [1]
        nextNum = 1
        nextIndex = 1  # 统计当前的已经找到的丑数个数

        p2 = p3 = p5 = 0

        while nextIndex < index:
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


s2 = Solution2()
print(s2.GetUglyNumber_Solution(10))
print(s2.GetUglyNumber_Solution(1500))
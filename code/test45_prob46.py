# 把数字翻译成字符串

# 0~25分别翻译为a~z.
# 以12为例, 可能有多种翻译. 可以翻译为bc也可以翻译为l
# 编程实现一个函数, 用来计算一个数字有多少种不同的翻译方法.

# 同leetcode91: 解码方法

# 动态规划解法
# 动态转换方程: f(i) = f(i-1) + g(i, i-1)*f(i-2)
class Solution1:
    def getTranslationCount(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) <= 0:
            return 0

        dp = [1 for i in range(0, len(s) + 1)]

        for i in range(2, len(dp)):
            if s[i - 2] != "0" and int(s[i - 2:i]) < 26:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        return dp[-1]


# 递归分析, 然后逆向解决, 使用循环提高效率
class Solution2:
    def GetTranslationCount(self, s):
        if not s or len(s) <= 0:
            return 0

        length = len(s)
        counts = [0] * length

        for i in range(length - 1, -1, -1):
            count = 0
            if i < length - 1:
                count = counts[i + 1]
            else:
                count = 1
            # print(count, counts)

            if i < length - 1:
                digit1 = int(s[i])
                digit2 = int(s[i + 1])
                converted = digit1 * 10 + digit2
                if converted >= 10 and converted <= 25:
                    if i < length - 2:
                        count = count + counts[i + 2]
                    else:
                        count = count + 1

            counts[i] = count
        count = counts[0]
        return count


print("解法一")
s = Solution1()
print(s.getTranslationCount(""))
print(s.getTranslationCount("12"))
# print(s.getTranslationCount("2"*100000))

print("解法二")
s2 = Solution2()
print(s2.GetTranslationCount(""))
print(s2.GetTranslationCount("12"))
# print(s2.GetTranslationCount("2" * 100000))

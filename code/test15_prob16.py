# 面试题16：数值的整数次方

# 底数为浮点型, 指数为整型, 要求不能使用库函数，不考虑大数问题.

# 规范的代码有下面三个要求：
# 1.能完成基本功能
# 2.输入边界值也能得到正确的输出
# 3.对各种不合规范的非法输入做了合适的处理


class Solution(object):
    def Power(self, base, exponent):

        g_InvalidInput = False
        if base == 0.0 and exponent < 0:
            g_InvalidInput = True  # 可用于判断错误来源
            # print("非法输入")
            return "非法输入"

        if exponent >= 0:
            return self.PowerWithUnsignedExponent(base, exponent)
        return 1.0 / self.PowerWithUnsignedExponent(base, -exponent)

    def PowerWithUnsignedExponent(self, base, exponent):
        # 这部分代码可以优化
        # result = 1.0
        # for i in range(1, exponent + 1):
        #     result *= base
        # return result

        # 更优的无符号指数幂的计算方法
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.PowerWithUnsignedExponent(base, exponent >> 1)  # 整数右移1位相当于对整数做2的除法
        res *= res

        # 判断如果是奇数的话
        if exponent & 0x1 == 1:  # 判断奇偶, 偶数的二进制的最后一位是0, 实现了求余运算的作用
            res *= base
        return res


s = Solution()
print(s.Power(2.0, 4))
print(s.Power(2.0, -3))
print(s.Power(0, -3))

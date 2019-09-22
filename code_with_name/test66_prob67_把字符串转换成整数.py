# 面试题67：把字符串转换成整数


# 思路分析：
# 主要考查的是考虑问题的全面性，如何保证代码的鲁棒性，针对各类输出能否妥善处理。
# 比如输入空字符串，返回什么；输入的字符串不合法，返回什么；如何区分这些不同的错误。----定义相应的全局变量
# 输入的字符串第一位可以有正负号， 如何处理。
# Python中不用考虑数值溢出， 只有位运算时才需要考虑。
class Solution(object):
    def StrToInt(self, s):

        # 如果输入为空
        if not s or len(s) <= 0:
            return 0

        numbers = ["%s" % i for i in range(10)]
        errorInput = False  # 字符串中有非法字符时设为True
        label = 1  # 用来表示符号位，表示输入的是一个正数还是负数
        sumvalue = 0

        for i in range(len(s)):
            if i == 0:
                if s[i] == "-":
                    label = -1
                    continue
                elif s[i] == "+":
                    continue

            if s[i] not in numbers:
                errorInput = True
                sumvalue = 0
                return sumvalue
            else:
                sumvalue = sumvalue * 10 + numbers.index(s[i])

        return sumvalue * label

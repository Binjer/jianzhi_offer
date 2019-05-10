# 不用加减乘除做加法

# 使用位运算．
# Python中位运算要判断是否越界

class Solution:
    def Add(self, num1, num2):
        # write code here

        while num2:
            # 后面这个与运算是为了防止越界
            sum_ = (num1 ^ num2) & 0xffffffff
            carry = ((num1 & num2) << 1) & 0xffffffff
            # 用num1把二进制对应位的和记录下来
            num1 = sum
            # num2记录进位, 如果不为0, 要继续把进位加到sum_上去_
            num2 = carry

        # 0x7fffffff是32位能表示的最大正数
        # 如果num1比它还大，说明num1是一个负数，要把它最高位置为0， 然后取反
        if num1 > 0x7fffffff:
            return ~(num1 ^ 0xffffffff)
        return num1

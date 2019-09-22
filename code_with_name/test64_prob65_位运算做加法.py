# 面试题65：不用加减乘除做加法


# 使用位运算．
# 第一步：二进制对应位相加，不计进位(二进制中的相加是异或运算);
# 第二步：记下进位;
# 第三步：把前面两步的结果相加。

# Python中位运算要判断是否越界
class Solution(object):
    def Add(self, num1, num2):

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

# 补充：二进制的加法要实现的目的是：0,0 = 0, 0,1 = 1, 1,0 = 1, 1,1 = 0.不难看出这是异或运算
#      二进制的进位要实现的目的是：0,0 = 0, 0,1 = 0, 1,0 = 0, 1,1 = 1.不难看出这是与运算


# 相关问题：不使用第三个变量，交换两个变量的值
# 方法一：
# a = a + b
# b = a - b
# a = a - b

# 方法二：
# a = a ^ b
# b = a ^ b
# a = a ^ b

# python中还可以利用赋值运算
# a, b = b, a

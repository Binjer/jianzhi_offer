# 面试题15：二进制中1的个数

# 位运算有五种：与、或、非、左移(每移一位相当于*2)和右移(每移一位相当于/2)


class Solution(object):
    def NumberOf1(self, n):
        # 方法一
        # return bin(n&0xffffffff).count("1")

        # 方法二：循环的次数等于整数二进制的位数
        # count = 0
        # flag = 1
        # while flag < 2 ** 31:  # 这里flag的最大值是跟二进制表示的位数有关的
        #     if n & flag:
        #         count += 1
        #     flag <<= 1
        #
        # return count

        # 方法三：循环的次数等于二进制中1的位数
        # 把一个整数减去1再与自身做与运算，相当于把这个整数的二进制中最右边的1变成了0
        # 二进制中有多少个1，可以做多少次这样的运算。
        count = 0
        while n:
            n = n & (n - 1)
            count += 1

        return count


s = Solution()
print(s.NumberOf1(1000000))

# 利用栈来完成进制转换
from pythonds.basic.stack import Stack


def tenToBase(n, base):
    s = Stack()
    while n > 0:
        s.push(n % base)
        n = n // base

    binString = ""
    while not s.isEmpty():
        binString += str(s.pop())
    return binString

# print(tenToBase(64, 2))


# 题目变形: 用一条语句判断一个整数是不是2的整数次方:
# 如果一个数是2的整数次方, 那么它的二进制表示中只有一位是1
# n & (n-1) == 0

# 题目变形2: 给定两个数m, n, 计算需要改变m的二进制中多少位才能得到n
# 思路: 先计算m和n的异或, 再统计异或结果中1的个数(异或为1表示两个数该位不同)

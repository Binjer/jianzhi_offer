class Solution:
    def NumberOf1(self, n):
        # write code here

        # 方法一
        # return bin(n&0xffffffff).count("1")

        # 方法二
        count = 0
        while n:
            n = n & (n - 1)
            count += 1

        return count


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

# 题目变形2: 给定两个数m, n, 计算需要改变m的二进制中多少位才能得到n
# 思路: 先计算m和n的异或, 再统计异或结果中1的个数(异或为1表示两个数该位不同)

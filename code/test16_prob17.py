# 面试题17：打印从1到n位的十进制中的所有数,n代表有几位

# 大数问题


# 用字符串模拟数字加法来做
class Solution1(object):
    # 打印从1到n位的最大数的所有数
    def Print1ToMaxOfNDigits(self, n):
        if n <= 0:
            return

        num = ["0"] * n

        while not self.increment(num):
            self.print_num(num)

    def increment(self, num):
        # 超过n位数时设为1
        overFlow = 0
        # 是否进位
        carry = 0
        length = len(num)

        # 字符串模拟数字的加法
        for i in range(length - 1, -1, -1):
            # 把字符串转换成数字进行运算
            number = ord(num[i]) - ord("0") + carry

            if i == length - 1:
                number += 1

            if number >= 10:
                if i == 0:
                    overFlow = 1
                else:
                    number -= 10
                    carry = 1
            else:
                carry = 0

            # 把运算完的数字转换成字符串
            num[i] = chr(ord("0") + number)

        return overFlow

    def print_num(self, num):
        string_num = "".join(num)
        length = len(num)

        for i in range(length):
            if string_num[i] != "0":
                print(string_num[i:])
                break


# 其实题目就是要n个从0到9的全排列，用递归很容易实现
class Solution2(object):
    def Print1ToMaxOfNDigits(self, n):

        if n <= 0:
            return

        number = ["0"] * n

        for i in range(10):
            number[0] = str(i)
            self.Recursive(number, n, 0)

    def Recursive(self, number, length, index):
        if index == length - 1:
            self.PrintNumber(number)
            return

        for i in range(10):
            number[index + 1] = str(i)
            self.Recursive(number, length, index + 1)

    def PrintNumber(self, number):
        # 此处的number为一个str类型的数组，每个数组元素是一个0-9之间数字的字符串形式
        # isbeginning0 = True
        # length = len(number)
        # for i in range(length):
        #     if isbeginning0 and number[i] != 0:
        #         isbeginning0 = False
        #     if not isbeginning0:
        #         print(number[i], end="")  # python默认换行，加上end去掉这种默认
        # print('\t')

        # 这种是不打印前面的0的方法
        string_num = "".join(number)
        length = len(string_num)

        for i in range(length):
            if string_num[i] != "0":
                print(string_num[i:])
                break  # break是跳出本次循环, 比如[0, 9, 8], 如果不用break会依次打印出98, 8

        # return


# if __name__ == "__main__":
#     # Solution1().Print1ToMaxOfNDigits(3)
#     # Solution2().Print1ToMaxOfNDigits(3)


# 相关题目：前面的代码中，我们都是用一个char型字符表示十进制数字的一位。
# 8个bit的char型字符最多能表示256个字符，而十进制数字只有0-9的10个数字。
# 因此用char型字符串来表示十进制的数字并没有充分利用内存，有一些浪费。
# 有没有更高效的方式来表示大数。
# 答：BitMap算法，尤其是处理大数据时十分有用，可以节省空间

# 2)定义一个函数，在该函数中可以实现任意两个整数的加法。由于没有限定输入
# 两个数的大小范围，我们也要把它当做大数问题来处理。在前面的代码的第一个
# 思路中，实现了在字符串表示的数字上加1的功能，我们可以参考这个思路实现
# 两个数字相加功能，另外还有一个需要注意的问题：如果输入的数字中有负数，
# 我们应该怎么处理？
# 答：同理可实现减法，有一个负号时先确定减数与被减数，有两个负号先调用加法，最后结果再添加一个负号


# 下面是字符串实现的加法(参考思路即可)
def add_by_str(a, b):
    l1 = len(a)
    l2 = len(b)

    # 字符串在python中是不可变类型，所以先转为list
    a = list(a)
    b = list(b)

    c = [0] * (max(l1, l2) + 1)  # c比两者中更长的那个数长一位的原因在于可能有进位

    if l1 >= l2:
        index1 = l1 - 1
        index2 = l2 - 1

        while index1 >= 0 and index2 >= 0:
            index_sum = int(a[index1]) + int(b[index2]) + c[index1 + 1]
            less = index_sum - 10
            c[index1 + 1] = index_sum % 10
            c[index1] = 1 if less >= 0 else 0

            index1 -= 1
            index2 -= 1

        while index1 >= 0:
            index_sum = int(a[index1]) + c[index1 + 1]
            less = index_sum - 10
            c[index1 + 1] = index_sum % 10
            c[index1] = 1 if less >= 0 else 0
            index1 -= 1
    else:
        index1 = l1 - 1
        index2 = l2 - 1

        while index1 >= 0 and index2 >= 0:
            index_sum = int(a[index1]) + int(b[index2]) + c[index2 + 1]
            less = index_sum - 10
            c[index2 + 1] = index_sum % 10
            c[index2] = 1 if less >= 0 else 0

            index1 -= 1
            index2 -= 1

        while index2 >= 0:
            index_sum = int(b[index2]) + c[index2 + 1]
            less = index_sum - 10
            c[index2 + 1] = index_sum % 10
            c[index2] = 1 if less >= 0 else 0
            index2 -= 1

    c = [str(i) for i in c]
    for i in range(len(c)):
        if c[i] != "0":
            sum_str = "".join(c[i:])
            return sum_str


# b = "2234"
# a = "67891"
a = "22341748783187478748431981984587537813843919889518951"
b = "67891151535616541781849854981489148941511355"
print(add_by_str(a, b))

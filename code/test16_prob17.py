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


if __name__ == "__main__":
    # Solution1().Print1ToMaxOfNDigits(3)
    Solution2().Print1ToMaxOfNDigits(3)

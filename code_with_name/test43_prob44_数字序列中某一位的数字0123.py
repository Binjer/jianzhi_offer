# 面试题44：数字序列中某一位的数字

# 数字以0123456789101112131415……的格式序列化到一个字符序列中(0~n)。
# 在这个序列中，第5位(从0开始计数)是5，第13位是1，第19位是4等等。
# 请编写一个函数，求任意第n位对应的数字


class Solution1(object):
    def digitAtIndex(self, n):

        index = n
        if index < 10:
            return index

        # 数字的位数
        digits = 1
        while True:
            numbers = self.count_of_integers(digits)
            if index < numbers * digits:
                return self.helper(index, digits)
            index -= digits * numbers
            digits += 1

    # 这个函数统计m位的数字共有多少个
    def count_of_integers(self, digits):
        return 9 * 10 ** (digits - 1)

    def helper(self, index, digits):
        begin_num = self.begin_number(digits)  # 找到对应位数的第一个数是什么

        if index == 0:
            return str(begin_num)[0]

        # 在这个位数中要跳过多少个数
        integer = (index - 1) // digits
        # 找到对应数的对应位数
        yu = (index - 1) % digits

        return int(str(integer + begin_num)[yu])

    def begin_number(self, digits):
        if digits == 1:
            return 0  # 一位数开始是0不是1
        else:
            return 10 ** (digits - 1)  # 两位数第一个是10，三位数第一个是100


s1 = Solution1()
print(s1.digitAtIndex(13))  # 1
print(s1.digitAtIndex(19))  # 4


# 解法二: 更简洁的写法, 思路其实和解法一差不多
class Solution2(object):
    def digitAtIndex(self, n):
        if n < 10:
            return n

        digit = 2
        i = 1

        n = n - 9
        pos = 9

        while n - 90 * i * digit > 0:
            n -= 90 * i * digit
            pos += 90 * i * digit

            i *= 10
            digit += 1

        i *= 10
        res = int(str(i + (n - 1) // digit)[(n - 1) % digit])

        return res


# s2 = Solution2()
# print(s2.digitAtIndex(10))
# print(s2.digitAtIndex(11))
# print(s2.digitAtIndex(12))
# print(s2.digitAtIndex(13))
# print(s2.digitAtIndex(14))
# print(s2.digitAtIndex(15))
# print(s2.digitAtIndex(16))
# print(s2.digitAtIndex(17))


# 面试提45：把数组排成最小的数


# 暴力解法一, 直接完成全排列, 再选出最小的一个
class Solution:
    def PrintMinNumber(self, numbers):

        import itertools
        if len(numbers) <= 0:
            return ""
        str_numbers = [str(i) for i in numbers]
        premu = itertools.permutations(str_numbers)
        res = [''.join(i) for i in premu]

        return min(res)


# 解法二:
# 将数组元素改为字符串表示, 并定义一种字符串的比较方法
# 比如对两个字符串str1="6", str2="53",
# 因为653>536, 所以我们认为str1 > str2(这就实现了字符串的比较)，把小的字符串排前面就组成了最小的数

# python2.x中的简洁写法
# class Solution21:
#     def PrintMinNumber(self, numbers):
#
#         if len(numbers) <= 0:
#             return ""
#
#         str_numbers = [str(i) for i in numbers]
#
#         res = sorted(str_numbers, cmp=lambda x, y: cmp(x + y, y + x))
#
#         return "".join(res)


# python3.x的写法
class Solution22(object):
    def PrintMinNumber(self, numbers):

        string = [str(num) for num in numbers]

        # 冒泡排序(当然也可以用其它的排序)
        for j in range(len(numbers) - 1, 0, -1):
            for i in range(j):
                if self.theMax(string[i], string[i + 1]) == string[i]:
                    string[i], string[i + 1] = string[i + 1], string[i]

        res = "".join(string)

        return res

    # 两个字符串的比较
    def theMax(self, str1, str2):
        '''定义字符串比较函数'''
        return str1 if str1 + str2 > str2 + str1 else str2


# 这道题可能还会考察从数学上证明我们的解决方案，要证明的内容有：
# 1.我们定义了一个比较两个字符串大小的规则，这种规则是不是有效的？
# 2.我们定义的是比较两个字符串大小的规则，却用它来排序一个含有多个数字的数组，最终拼接数组中的所有字符串得到的是不是真的就是最小的字符串？

# 一个有效的比较规则需要3个条件：自反性，对称性，传递性
# 自反性和对称性很容易证明，传递性证明见书上p229

# 第2部分的证明用反证法即可

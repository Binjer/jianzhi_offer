# 把数组排成最小的数

# 暴力解法一, 直接完成全排列, 再选出最小的一个
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        import itertools
        if len(numbers) <= 0:
            return ""
        str_numbers = [str(i) for i in numbers]
        premu = itertools.permutations(str_numbers)
        res = [''.join(i) for i in premu]
        return min(res)


# 解法二:
# 将数组元素改为字符串表示, 并定义一种字符串的比较方法

# python2.x中的简洁写法
# class Solution2:
#     def PrintMinNumber(self, numbers):
#         # write code here
#
#         if len(numbers) <= 0:
#             return ""
#
#         str_numbers = [str(i) for i in numbers]
#
#         res = sorted(str_numbers, cmp=lambda x, y: cmp(x + y, y + x))
#
#         return "".join(res)


class Solution3:
    def PrintMinNumber(self, numbers):
        # write code here

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

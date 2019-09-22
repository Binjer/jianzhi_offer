# 面试题58：翻转字符串

# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
# 例如输入"I am a student.", 则输出"student. a am I"


# 利用Python的split方法和切片特性很容易实现.
# temp = s.split()
# if len(temp) == 0:
#     return s
# return " ".join(temp[::-1])


# 常规解法: 两次翻转: 先翻转整个字符串, 再翻转句子中的每个单词
# 注意python中字符串是不可变类型
class Solution11(object):
    def ReverseSentence(self, s):

        if not s or len(s) <= 0:
            return ""

        li = list(s)
        li = self.reverse(li)

        start = 0
        end = 0
        listTemp = []

        while end < len(li):
            if end == len(li) - 1:
                listTemp.append(self.reverse(li[start:]))
                break

            if li[start] == " ":
                start += 1
                end += 1
                listTemp.append(" ")
            elif li[end] == " ":
                listTemp.append(self.reverse(li[start:end]))
                start = end
            else:
                end += 1

        res = ""
        for i in listTemp:
            res += "".join(i)

        return res

    def reverse(self, str_li):
        start = 0
        end = len(str_li) - 1

        while start < end:
            str_li[start], str_li[end] = str_li[end], str_li[start]
            start += 1
            end -= 1

        return str_li


s = Solution11()
print(s.ReverseSentence("i am a student."))


# 引申题目：左旋转字符串
# 左旋转字符串可以看成是先将字符串分成两部分，先把两部分分别翻转，再翻转整个字符串
class Solution21(object):
    def LeftRotateString(self, s, n):

        if not s or len(s) <= 0:
            return ''

        # 这里应明确题目要求n是不是可以比字符串长度大
        if len(s) <= n:
            n = n % len(s)

        # s1 = list(s)
        # listTemp = []
        # listTemp.append(self.reverseCore(s1[:n]))
        # listTemp.append(self.reverseCore(s1[n:]))
        # # print(listTemp)
        #
        # # sum()可以用来给二维列表进行降维
        # # 可以实现n维~n-1维的降维. 因此可以嵌套使用
        # s2 = self.reverseCore(sum(listTemp, []))
        # # print(s2)
        # res = "".join(s2)
        #
        # return res

        s_li = list(s)
        left = self.reverseCore(s_li[:n])
        right = self.reverseCore(s_li[n:])

        res = self.reverseCore(left + right)

        res = "".join(res)

        return res

    def reverseCore(self, str_li):
        # str_li是一个列表
        start = 0
        end = len(str_li) - 1
        while start < end:
            str_li[start], str_li[end] = str_li[end], str_li[start]
            start += 1
            end -= 1

        return str_li


s = Solution21()
print(s.LeftRotateString("abcdefg", 2))

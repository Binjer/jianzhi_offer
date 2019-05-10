# 翻转字符串

# 利用Python的split方法和切片特性很容易实现.
# temp = s.split()
# if len(temp) == 0:
#     return s
# return " ".join(temp[::-1])


# 常规解法: 两次翻转: 先翻转整个字符串, 再翻转句子中的每个单词
class Solution(object):
    def ReverseSentence(self, s):
        # write code here
        if len(s) <= 0 or not s:
            return s

        s = list(s)
        s = self.reverseCore(s)

        pStart = 0
        pEnd = 0
        listTemp = []

        while pEnd < len(s):
            if pEnd == len(s) - 1:
                listTemp.append(self.reverseCore(s[pStart:]))
                break

            if s[pStart] == ' ':
                pStart += 1
                pEnd += 1
                listTemp.append(' ')

            elif s[pEnd] == ' ':
                listTemp.append(self.reverseCore(s[pStart:pEnd]))
                pStart = pEnd
            else:
                pEnd += 1
        print(listTemp)

        result = ''
        for i in listTemp:
            result += ''.join(i)
        return result

    def reverseCore(self, string):
        # string是一个列表
        start = 0
        end = len(string) - 1
        while start < end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1

        return string


# s = Solution()
# print(s.ReverseSentence("i am a student."))

# 坐旋转字符串
class Solution22:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or len(s) <= 0:
            return ''

        # 这里应明确题目要求n是不是可以比字符串长度大
        if len(s) <= n:
            n = n % len(s)

        s1 = list(s)
        listTemp = []
        listTemp.append(self.reverseCore(s1[:n]))
        listTemp.append(self.reverseCore(s1[n:]))
        # print(listTemp)

        # sum()可以用来给二维列表进行降维
        # 可以实现n维~n-1维的降维. 因此可以嵌套使用
        s2 = self.reverseCore(sum(listTemp, []))
        # print(s2)

        res = "".join(s2)

        return res

    def reverseCore(self, string):
        # string是一个列表
        start = 0
        end = len(string) - 1
        while start < end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1

        return string


s = Solution22()

print(s.LeftRotateString("abcdefg", 8))

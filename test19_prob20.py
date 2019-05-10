# 表示数值的字符串
# 思路解析:
# 数值行字符串可以表示为A.B(e/E)C
# 其中A, B, C代表3个子串, 其中A和C的首位可以是正负号或者0~9, 其余位只能是0~9, B的每一位都只能是0~9

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code
        if not s or len(s) <= 0:
            return False

        alist = [i.lower() for i in s]
        if "e" in alist:
            indexOfe = alist.index("e")
            frontList = alist[:indexOfe]
            behindList = alist[indexOfe + 1:]
            if "." in behindList or len(behindList) == 0:
                return False
            behind = self.isNumerical(behindList)
            front = self.isNumerical(frontList)
            return behind and front
        else:
            return self.isNumerical(alist)

    def isNumerical(self, alist):
        dotNum = 0
        allowNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "."]
        for i in range(len(alist)):
            if alist[i] not in allowNum:
                return False
            if alist[i] == ".":
                dotNum += 1
            if alist[i] in "+-" and i != 0:
                return False

        if dotNum > 1:
            return False

        return True


s = Solution()
print(s.isNumeric("+789123.4155E67812"))
print(s.isNumeric("+789123.4155E67812."))
print(s.isNumeric("+789123.4155E6E7812"))


class Solution2(object):
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s or len(s) == 0:
            return False

        # 是否有e
        hasE = False
        # 是否有小数
        isDecimal = False
        # 是否有+-符号
        hasSign = False

        for i in range(len(s)):
            # 如果有e,只能有一个e且不能是最后一个
            if s[i] == "e" or s[i] == "E":
                if hasE or i == len(s) - 1:
                    return False
                hasE = True
            # 小数点不能重复出现.
            # 这里隐藏着一个逻辑是: 前面的语句是先判断是否有e的, 如果有e了, 后面就不能出现小数点了
            elif s[i] == ".":
                if hasE or isDecimal:
                    return False
                isDecimal = True

            elif s[i] == "-" or s[i] == "+":
                # 重复出现符号时，必须跟在e后面
                if hasSign and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
                # 重复出现符号时，必须跟在e后面
                if not hasSign and i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
                hasSign = True
            elif s[i] < "0" or s[i] > "9":
                return False
        return True

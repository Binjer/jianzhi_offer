# 第一个只出现一次的字符

# 解法一: 两层for循环
class Solution1:
    def firstNotRepeatingChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) <= 0:
            return "#"

        for i in range(len(s)):
            count = 0
            for j in range(len(s)):
                if s[i] == s[j]:
                    count += 1

            if count == 1:
                return s[i]

        return "#"


# 解法二
# 字符串中只出现一次的字符
# 先用一个哈希表记录每个字符出现的次数
# 再遍历一次字符串找到第一个只出现一次的字符,没有的话则返回要求的值
class Solution(object):
    def firstNotRepeatingChar(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Python中字符串有count函数,十分方便
        # for i in s:
        #     if s.count(i) == 1:
        #         return i
        #
        # return "#"

        hashTable = {}

        for i in range(len(s)):
            if s[i] in hashTable:
                hashTable[s[i]] += 1
            else:
                hashTable[s[i]] = 1

        for i in range(len(s)):
            if hashTable[s[i]] == 1:
                return s[i]

        return "#"


def delDuplicationCharacter(s):
    if not s or len(s) <= 0:
        return 0

    myDict = {}
    newStr = ""

    for i in range(len(s)):
        if s[i] not in myDict:
            myDict[s[i]] = 1
            newStr += s[i]

    return newStr


# print(delDuplicationCharacter("aaaaa"))


# 题目二:
# 字符流中第一个只出现一次的字符
class Solution2(object):
    def __init__(self):
        self.alist = []
        self.char_dict = {}

    def firstAppearingOnce(self):
        """
        :rtype: str
        """
        # while len(self.alist) > 0 and self.char_dict[self.alist[0]] == -1:
        #     self.alist.pop(0)
        #
        # if len(self.alist) > 0:
        #     return self.alist[0]
        # return "#"

        # 更简单的写法: 就是根据字符串顺序遍历字典找到第一个值不为-1的键
        for i in range(len(self.alist)):
            if self.char_dict[self.alist[i]] != -1:
                return self.alist[i]

        return "#"

    def insert(self, char):
        """
        :type char: str
        :rtype: void
        """
        if char not in self.char_dict:
            self.alist.append(char)
            self.char_dict[char] = 1
        else:
            self.char_dict[char] = -1

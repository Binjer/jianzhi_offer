# 面试题50：第一个只出现一次的字符

# 找到在字符串中第一个只出现一次的字符
# 例如输入"abaccdeff", 则输出"b"


# 解法一:
# 两层for循环, 时间复杂度O(n2)
class Solution11(object):
    def firstNotRepeatingChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) <= 0:
            return -1

        for i in range(len(s)):
            count = 0
            for j in range(len(s)):
                if s[i] == s[j]:
                    count += 1

            if count == 1:
                return s[i]

        return -1


# 解法二
# 字符串中只出现一次的字符
# 先用一个哈希表记录每个字符出现的次数
# 再遍历一次字符串找到第一个只出现一次的字符,没有的话则返回要求的值
# 时间复杂度O(n), 空间复杂度O(n)
class Solution12(object):
    def firstNotRepeatingChar(self, s):
        """
        :type s: str
        :rtype: str
        """

        # python内置函数
        # python中字符串有count函数,十分方便
        # for i in s:
        #     if s.count(i) == 1:
        #         return i
        #
        # return -1

        hashTable = {}

        for i in range(len(s)):
            if s[i] in hashTable:
                hashTable[s[i]] += 1
            else:
                hashTable[s[i]] = 1

        for i in range(len(s)):
            if hashTable[s[i]] == 1:
                return s[i]

        return -1


# 扩展题目1：定义一个函数，输入两个字符串，从第一个字符串中删除在第二个字符串中出现过的所有字符
def delRepeatedStr(s1, s2):
    # 这里只是示范一下需要处理异常的输入，具体情况要按照题目要求
    if not s1 or not s2:
        return -1

    hashTable = {}
    for i in range(len(s2)):
        if s2[i] in hashTable:
            continue
        else:
            hashTable[s2[i]] = 1

    # 注意在pyhton中字符串是不可变类型
    # 这里是先将字符串转换为列表处理完毕后再转换为字符串，也可以直接新建一个字符串，扩展题目2中给出了示范
    s1_li = list(s1)

    for i in range(len(s1_li)):
        if s1_li[i] in hashTable:
            s1_li[i] = ""

    s1 = "".join(s1_li)

    return s1


# print(delRepeatedStr("We are students", "aeiou"))


# 扩展题目2：删除字符串中所有重复出现的字符(只保留一个)
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

# 扩展题目3：判断两个单词是否为变位词
# 遍历第一个单词，得到每个字符出现的次数存入哈希表，
# 遍历第二个单词，如果某个字符出现在哈希表中，则次数减去1.
# 最后如果哈希表中所有值都是0，那么这两个字符串互为变位词。
# 注意：要考虑listen， silentence这种情况，也就是遍历第二个单词的时候，如果某个字符不在哈希表中，那么则返回False


# 题目二:
# 字符流中第一个只出现一次的字符
class Solution21(object):
    def __init__(self):
        self.alist = []  # 保存字符流
        self.char_dict = {}  # 保存字符是否出现过

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
        self.alist.append(char)

        if char not in self.char_dict:
            self.char_dict[char] = 1
        else:
            self.char_dict[char] = -1

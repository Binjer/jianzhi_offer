# 最长不含重复字符的子字符串

# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长字符串的长度。
# 假设字符串中只包含‘a’-‘z’的字符。
# 例如，在字符串“arabcacfr”中，最长的不含重复字符的子字符串是“acfr”，长度为4。


class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        pos = [-1] * 26
        curLength = 0

        for i in range(len(s)):
            prevIndex = pos[ord(s[i]) - ord("a")]
            if prevIndex < 0 or i - prevIndex > curLength:
                curLength += 1
            else:
                if curLength > maxLength:
                    maxLength = curLength

                curLength = i - prevIndex

            pos[ord(s[i]) - ord("a")] = i

            if curLength > maxLength:
                maxLength = curLength

        return maxLength


# s1 = Solution1()
# print(s1.lengthOfLongestSubstring("arabcacfr"))


# 解法思路:
# 设定一个起始指针, 如果出现了前面的字符就把起始指针移到前面的重复字符位置+1
# 否则最大长度就是i-start+1(这是考虑到aaaa这种情况)
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0  # 代表最长字符串的开始位置, 一旦出现重复字符串, 会变化
        maxLength = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength


s2 = Solution2()
print(s2.lengthOfLongestSubstring("arabcacfr"))
print(s2.lengthOfLongestSubstring("aaaaaa"))
print(s2.lengthOfLongestSubstring("abccbabc"))
print(s2.lengthOfLongestSubstring("aaadsvdadfa"))


# 动态规划
class Solution3(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) <= 0:
            return 0

        d = {}
        dp = [0] * len(s)

        # 正向动态规划
        for i in range(len(s)):
            # 如果当前字符还没出现过, 那么f(i) = f(i-1) + 1
            if s[i] not in d:
                # 这里利用了Python中列表的一个特殊性质, 前面初始化必须为0才可以
                dp[i] = dp[i - 1] + 1
            # 如果出现了重复字符
            else:
                # 如果重复字符之间的距离d大于f(i-1), 仍有f(i) = f(i-1) + 1
                if i - d[s[i]] > dp[i - 1]:
                    dp[i] = dp[i - 1] + 1
                # 如果重复字符之间的距离d小于f(i-1), 此时有f(i) = d
                else:
                    dp[i] = i - d[s[i]]
            d[s[i]] = i

        return max(dp)


s3 = Solution3()
print(s3.lengthOfLongestSubstring("arabcacfr"))
print(s3.lengthOfLongestSubstring("aaaaaa"))
print(s3.lengthOfLongestSubstring("abccbabc"))

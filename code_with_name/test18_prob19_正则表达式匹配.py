# 面试题19：正则表达式匹配
# .可以匹配任意一个字符, *代表前面的字符可以出现0~任意次

# 思路分析: 递归的思想来实现
# 当模式字符串(pattern)中的第二个字符串是*时:
# 如果字符串和模式字符串的第一个字符匹配了: 就会有三种情况:
# 1, 字符串不动, 模式字符串向后移动两位;
# 2. 字符串向后移动一位, 模式字符串不动
# 3. 字符串向后移动一位, 模式字符串向后移动两位 (事实上这一种情况被前两种的并集包括了)

# 如果字符串和模式字符串的第一个字符不匹配, 只有一种情况: 就是将模式字符串往后移动两位, 继续递归调用

# 当p中第二个字符串不是*:
# 如果s[0] == p[0] 或者 p[0] = ".", 那么字符串和模式字符串都向后移动一位递归调用

# 如果s[0] != p[0], 返回False, 即不匹配


# python中is 主要是判断 2 个变量是否引用的是同一个对象
# python中== 主要是判断 2 个变量的值是否相等


class Solution(object):
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code_with_name here
        p = pattern

        if s == p:
            return True

        if not p:
            return False

        # 这部分是pattern第二位是*的情况，需要递归解决
        if len(p) > 1 and p[1] == "*":
            if s and (s[0] == p[0] or p[0] == "."):
                return self.match(s, p[2:]) or self.match(s[1:], p) or self.match(s[1:], p[2:])
            else:
                return self.match(s, p[2:])
        # 这部分是pattern第二位不是*的情况，只需要判断第一位是不是相同或者pattern的第一位是不是.就可以了
        elif s and (s[0] == p[0] or p[0] == "."):
            return self.match(s[1:], p[1:])

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.match("", "."))

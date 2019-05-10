# 替换字符串中的空格
# python中字符串有split()方法, 结合join可完成用任意新字符替代字符串中的特定字符 "%20".join(s.split(" "))
# 也可以直接使用 字符串.replace("旧字符", "新字符")方法 s.replace(" ", "%20")


# 书中提供的原始思路, 跟字符串的编码有关

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # 计算空格数量
        s = list(s)
        count = 0
        for e in s:
            if e == ' ':
                count += 1

        p1 = len(s) - 1  # p1为原始字符串数组末尾的index
        # 求新数组长度
        s += [None] * (count * 2)
        p2 = len(s) - 1  # p2为新字符串数组末尾的index
        while p1 >= 0:
            if s[p1] == ' ':
                for i in ['0', '2', '%']:
                    s[p2] = i
                    p2 -= 1
            else:
                s[p2] = s[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(s)




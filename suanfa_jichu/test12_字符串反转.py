# 给定一个字符串，字符串包含数字、大小写字母以及括号（包括大括号，中括号，小括号），括号可以嵌套，即括号里面可以出现数字和括号。

# 按照如下规则对字符串进行展开，不需要考虑括号不成对的问题，不考虑数字后面没有括号的情况，即 2a2(b)不考虑。
#
# 数字表示括号里的字符串重复的次数，展开后的字符串不包含括号
# 将字符串进行逆序展开

s1 = "(AB(CD)E)"
s2 = "(AB(CD)E)(AB(CD))"
s3 = "a(bc(de)fg)hijk"  # 输出：agfdecbhijk
s4 = "(a(bc(de)fg)(AB(CD)))"

s = "abc2{de3[fg]}"


def reverse_str(str1):
    s1 = []

    for i in range(len(str1)):
        # 遇到右括号，需要逆序第一对括号里面的字符
        if str1[i] in ")]}":
            s2 = []

            # count = -1
            while s1[-1] not in "([{":
                s2.append(s1.pop())
                # count -= 1

            # 把右括号对应的左括号删除
            s1.pop()
            tmp2 = -1
            repeat = ""
            while s1[-1] in "0123456789":
                repeat += s1.pop()

            repeat = int(repeat[::-1])

            s2 = s2[::-1]
            s1 += s2 * repeat

        else:
            s1.append(str1[i])

    return "".join(s1[::-1])


print(reverse_str(s))

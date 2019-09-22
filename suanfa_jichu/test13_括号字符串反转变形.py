# 括号字符串反转

# s1 = "(AB(CD)E)"
# s2 = "(AB(CD)E)(AB(CD))"
# s3 = "a(bc(de)fg)hijk"  # 输出：agfdecbhijk
# s4 = "(a(bc(de)fg)(AB(CD)))"
#
#
# def reverse_str(str1):
#     res = []
#     s1 = []
#
#     for i in range(len(str1)):
#         # 遇到右括号，需要逆序第一对括号里面的字符
#         if str1[i] == ")":
#             s2 = []
#             count = -1
#             while s1[-1] != "(":
#                 s2.append(s1.pop())
#                 count -= 1
#
#             # 把右括号对应的左括号删除
#             s1.pop()
#             s1 += s2
#
#         else:
#             s1.append(str1[i])
#
#     return "".join(s1)
#
#
# print(reverse_str(s4))


# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     res = []
#     for i in range(n, 0, -1):
#         res.append(i)
#         tmp = res[0]
#         res.pop(0)
#         res.append(tmp)
#
#     for i in range(len(res)):
#         if i == len(res) - 1:
#             print(res[len(res) - i - 1], end='')
#         else:
#             print(res[len(res) - i - 1], end=' ')
#     print()


def fangzhen(li):
    res = []
    while len(li) > 0:
        tmp = li[0]
        li.pop(0)
        li.append(tmp)
        tmp2 = li[0]
        res.append(tmp2)
        li.pop(0)

    return res


li = [i for i in range(1, 11)]
proj = fangzhen(li)

res = [0] * 10
count = 1
for r in proj:
    res[r - 1] = count
    count += 1

print(res)

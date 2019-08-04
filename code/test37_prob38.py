# 面试题38：字符串的排列


# 书上的思路
class Solution1(object):
    def Permutation(self, ss):

        res = []
        if len(ss) == 0:
            return res

        charlist = list(ss)

        self.permutation(charlist, 0, res)

        res = [''.join(res[i]) for i in range(len(res))]
        # res.sort()

        return res

    def permutation(self, ss, begin, res):
        if begin == len(ss) - 1:
            res.append(ss[:])
        else:
            for i in range(begin, len(ss)):
                # 如果是重复字符，跳过
                if ss[begin] == ss[i] and begin != i:
                    continue
                else:
                    # 依次与后面每个字符交换
                    ss[begin], ss[i] = ss[i], ss[begin]
                    self.permutation(ss, begin + 1, res)
                    # 回到上一个状态
                    ss[begin], ss[i] = ss[i], ss[begin]


# s = Solution1()
# res = s.Permutation("abc")
# print(res)
# print(len(res))


class Solution2(object):
    """
    这一解法的思路在于每次从字符串的相同位置取出一个字母,并把他们拼接起来, 相当于把第一个字母和后面的字母依次交换了位置.
    缺点是结果是有重复的, 要再进行去重操作
    """

    def Permutation(self, ss):

        if not ss:
            return []
        res = []
        self.helper(ss, res, '')

        return res

        # return sorted(list(set(res)))

    def helper(self, ss, res, path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i] + ss[i + 1:], res, path + ss[i])


# s = Solution2()
# res = s.Permutation("aac")
# print(res)
# print(len(res))


# # 组合问题  这是combinations库的源代码
# def combinations(iterable, r):
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i + 1, r):
#             indices[j] = indices[j - 1] + 1
#         yield tuple(pool[i] for i in indices)
#
#
# res = []
# for i in combinations("abc", 2):
#     # print("".join(i))
#     res.append("".join(i))
# print(res)

# def list_zuhe(a1, mylist, res):
#     # 递归解法
#     if 2 == len(mylist):
#         # print(a1 + mylist[0] + mylist[1])
#         # print(a1 + mylist[1] + mylist[0])
#         res.append(a1 + mylist[0] + mylist[1])
#         res.append(a1 + mylist[1] + mylist[0])
#     else:
#         for i, j in enumerate(mylist):
#             # 切片操作后面加中括号带默认索引的话表示复制了一份,
#             # 不带的话就是单纯的引用
#             c = mylist[:]
#             c.pop(i)
#             list_zuhe(a1 + j, c, res)
#
#
# strs = 'abc'
# mylist = list(set(list(strs)))
# # mylist=['ab','c','123'] # 可以给定任意需要组合的list
# res = []
# list_zuhe('', mylist, res)
# print(res)

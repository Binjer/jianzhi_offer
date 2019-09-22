# 面试题5: 替换字符串中的空格


# 方法一：Python特性
# python中字符串有split()方法, 结合join可完成用任意新字符替代字符串中的特定字符 "%20".join(s.split(" "))
# 也可以直接使用 字符串.replace("旧字符", "新字符")方法 s.replace(" ", "%20")
class Solution1(object):
    def replaceSpace(self, s):
        if not s or len(s) == 0:
            return ""

        # return "%20".join(s.split(" "))
        return s.replace(" ", "%20")


# 方法二：
# 书中提供的原始思路, 跟字符串的编码有关
# 注意字符串在python中是不可变类型, 所以先创建一个列表, 最后将其转为字符串
class Solution2(object):
    def replaceSpace(self, s):

        if not s or len(s) == 0:
            return ""

        # 统计字符串中空格的个数
        count = 0
        for i in s:
            if i == " ":
                count += 1

        # 初始化一个长度和新字符串相同的列表
        newS_list = [0 for i in range(len(s))] + [0] * 2 * count

        p1 = len(s) - 1
        p2 = len(newS_list) - 1
        while p1 >= 0:
            if s[p1] == " ":
                for i in ["0", "2", "%"]:
                    newS_list[p2] = i
                    p2 -= 1
            else:
                newS_list[p2] = s[p1]
                p2 -= 1
            p1 -= 1

        newS = "".join(newS_list)

        return newS


# 相关题目：
# 有两个排序的数组A1和A2, 内存在A1的末尾有足够多的空间容纳A2
# 请实现一个函数, 将A2中所有的数字插入到A1中, 并且所有的数字仍是排序的
# 这里只是模拟了一下数组合并的过程, 如果按题目要求是不需要引入辅助数组的, 直接在A1的后面开始安排值即可
# 启发： 正向思路会有很多重复步骤时可以试试反向；
#       维护两个指针能够以O(n)合并两个排序数组
class Solution3(object):
    def mergeTwoOrderedArray(self, A1, A2):
        # 这里假设A1, A2如果输入是数组则不为空
        if not A1 or not A2:
            return

        length = len(A1) + len(A2)
        A = [0 for i in range(length)]

        p1 = len(A1) - 1
        p2 = len(A2) - 1
        p = len(A) - 1

        while p1 >= 0 and p2 >= 0:
            if A1[p1] == A1[p2]:
                A[p] = A2[p2]
                A[p - 1] = A1[p1]
                p -= 2
                p1 -= 1
                p2 -= 1
            elif A1[p1] > A2[p2]:
                A[p] = A1[p1]
                p -= 1
                p1 -= 1
            else:
                A[p] = A2[p2]
                p -= 1
                p2 -= 1

        return A

# s = Solution3()
# print(s.mergeTwoOrderedArray([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))

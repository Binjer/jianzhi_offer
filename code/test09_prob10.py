# 循环和递归
# 递归代码比较简洁. 缺点是函数调用时室友空间消耗的, 有可能会发生调用栈溢出


# 题目10: 斐波那契数列
# 递归的思路, 会造成大量的重复计算, 因此效率比较低

# 应用题目:
# 青蛙跳台阶
# 变态跳台阶
# 小矩形覆盖大矩形

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(500))


def fibonacci2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    f1 = 0
    f2 = 1
    # i = 2
    # while i <= n:
    #     fn = f1 + f2
    #     f1 = f2
    #     f2 = fn
    #     i += 1

    # for i in range(2, n + 1):
    #     fn = f1 + f2
    #     f1 = f2
    #     f2 = fn

    return f2


# print(fibonacci2(10))


# def quick_sort(alist, start, end):
#     if start >= end:
#         return
#
#         # 设定起始元素为基准元素
#     mid = alist[start]
#
#     low = start
#     high = end
#
#     while low < high:
#         while low < high and alist[high] >= mid:
#             high -= 1
#         alist[low] = alist[high]
#
#         while low < high and alist[low] <= mid:
#             low += 1
#         alist[high] = alist[low]
#
#     alist[low] = mid
#
#     quick_sort(alist, start, low - 1)
#     quick_sort(alist, low + 1, end)


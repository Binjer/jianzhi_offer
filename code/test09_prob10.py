# 循环和递归
# 递归代码比较简洁. 缺点是函数调用时室友空间消耗的, 有可能会发生调用栈溢出


# 题目10: 斐波那契数列
# 递归的思路, 会造成大量的重复计算, 因此效率比较低
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(5000))
# 会出现下面的错误：RecursionError: maximum recursion depth exceeded in comparison


# 这种情况, 我们可以用递归来帮助理解, 但是用循环来解决问题
def fibonacci2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    f1 = 0
    f2 = 1

    # 思路一
    # i = 2
    # while i <= n:
    #     fn = f1 + f2
    #     f1 = f2
    #     f2 = fn
    #     i += 1

    # 思路2
    for i in range(2, n + 1):
        fn = f1 + f2
        f1 = f2
        f2 = fn

    return f2


print(fibonacci2(1000))

# 应用题目:
# 青蛙跳台阶: 抽象出斐波那契数列表示
# f(n)=f(n-1)+f(n-2)

# 变态跳台阶:
# 1.递归分析：
# f(n)=f(n-1)+f(n-1)
# n比n-1多了一个台阶, 这一个台阶可以增加f(n-1)种跳法

# 2.动态规划的思想更容易理解
# 我们用f(n)来表示跳n级台阶的跳法数量，
# f(1)=1表示跳1级台阶的跳法数量;
# f(2)=2表示跳2级台阶的跳法数量;
# f(3)=f(2)+f(1)+1  我们可以递推出f(n)=f(n-1)+f(n-2)+ *** +f(1)+1 ,
#
# 而f(n-1)=f(n-2)+ *** +f(1)+1。
# 将两式想减可以求出递推公式，也即是 f(n)-f(n-1)=f(n-1)，即f(n)=2*f(n-1)

# 小矩形覆盖大矩形
# f(n)=f(n-1)+f(n-2)

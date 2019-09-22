# TODO 01背包问题(每件物品只有一件，要么取要么不取)

# 在N件物品取出若干件放在容量为W的背包里，每件物品的体积为W1，W2……Wn（Wi为整数），
# 与之相对应的价值为P1,P2……Pn（Pi为整数），求背包能够容纳的最大价值。


def bag_max_value(n, c, w, v):
    """
       测试数据：
       n = 6  物品的数量，
       c = 10 书包能承受的重量，
       w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
       v = [2, 3, 1, 5, 4, 3] 每个物品的价值
       """

    # 横坐标表示书包的容量
    # 纵坐标表示不同的物品
    # 初始化这里要根据题目的要求来，一般有两种不太一样的问法：
    # 一种要求恰好将背包装满；
    bag = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, len(bag[0])):
        bag[0][i] = float("-inf")

    # 一种只要不超过背包的限制即可
    # bag = [[0 for j in range(c + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):

            # 如果能够装下当前物体
            if j >= w[i - 1]:
                # 此时价值应该等于放第当前物体，不放当前物体的价值中较大值
                bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - w[i - 1]] + v[i - 1])
            # 装不下当前物体，最大价值就等于上一行的值
            else:
                bag[i][j] = bag[i - 1][j]

    # 优化一下，只用一个一维数组保存，不断更新即可
    # bag = [0 for i in range(c + 1)]
    # for i in range(1, n + 1):
    #     for j in range(c, 0, -1):
    #         if j >= w[i - 1]:
    #             bag[j] = max(bag[j], bag[j - w[i - 1]] + v[i - 1])

    return bag


n = 6
c = 10
w = [2, 2, 3, 1, 5, 2]
v = [2, 3, 1, 5, 4, 3]

print("01背包问题价值矩阵为：")
bag_value = bag_max_value(n, c, w, v)
for v in bag_value:
    print(v)


# print(bag_value)


def show(n, c, w, bag_value):
    print('最大价值为:', bag_value[n][c])
    x = [False for i in range(n)]
    j = c

    for i in range(n, 0, -1):
        if bag_value[i][j] > bag_value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]

    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i + 1, '个,', end='')


show(n, c, w, bag_value)


# TODO 02.多重背包问题(每件物品都有限制的件数)
# 可以很容易的转换为01背包问题，比如第5件物品有3件，那么就可以将它拆分成3件重量和体积都一样的物品，这样就是01背包问题了。
# 假设每种物品的数量为Ni件，那么多重背包问题可以转换为N=sum(Ni)件物品的01背包问题

# 优化：采用二进制分解
# 一个正整数n可以被分解成1,2,4,2**k-1,n-2**k+1,且1～n之内的所有整数都能被表示为分解出的某几个因子之和。
# 如13分解为1,2,4,6(6=13-2**3+1)

def binaryDecomposition(n):
    k = 0
    res = []
    while n - 2 ** (k + 1) + 1 > 0:
        res.append(2 ** k)
        k += 1
    res.append(n - 2 ** k + 1)

    return res


print("13的二进制分解结果为：", binaryDecomposition(13))


# TODO 03.完全背包问题(每件物品都有任意件)
# 只需要修改01背包问题的状态转移方程即可
# bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - w[i - 1]] + v[i - 1])改为
# bag[i][j] = max(bag[i - 1][j], bag[i][j - w[i - 1]] + v[i])


def bag_max_value(n, c, w, v):
    """
       测试数据：
       n = 6  物品的数量，
       c = 10 书包能承受的重量，
       w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
       v = [2, 3, 1, 5, 4, 3] 每个物品的价值
       """

    # 横坐标表示书包的容量
    # 纵坐标表示不同的物品
    # 初始化这里要根据题目的要求来，一般有两种不太一样的问法：
    # 一种要求恰好将背包装满；
    bag = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, len(bag[0])):
        bag[0][i] = float("-inf")

    # 一种只要不超过背包的限制即可
    # bag = [[0 for j in range(c + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):

            # 如果能够装下当前物体
            if j >= w[i - 1]:
                # 此时价值应该等于放第当前物体，不放当前物体的价值中较大值
                bag[i][j] = max(bag[i - 1][j], bag[i][j - w[i - 1]] + v[i - 1])
            # 装不下当前物体，最大价值就等于上一行的值
            else:
                bag[i][j] = bag[i - 1][j]

    return bag


n = 6
c = 10
w = [2, 2, 3, 1, 5, 2]
v = [2, 3, 1, 5, 4, 3]

print("完全背包问题价值矩阵为：")
bag_value = bag_max_value(n, c, w, v)
for v in bag_value:
    print(v)


# TODO 04.混合背包问题(有的物品有有限件， 有的物品有无限件)
# 只需要修改01背包问题的状态转移方程即可
# bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - w[i - 1]] + v[i - 1])改为
# bag[i][j] = max(bag[i - 1][j], bag[i][j - w[i - 1]] + v[i])


def bag_max_value(n, c, w, v, s):
    """
       测试数据：
       n = 6  物品的数量，
       c = 10 书包能承受的重量，
       w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
       v = [2, 3, 1, 5, 4, 3] 每个物品的价值
       s = [1, 1, 1, float("inf"), 1,1]  每个物品的数量
       """

    # 横坐标表示书包的容量
    # 纵坐标表示不同的物品
    # 初始化这里要根据题目的要求来，一般有两种不太一样的问法：
    # 一种要求恰好将背包装满；
    bag = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, len(bag[0])):
        bag[0][i] = float("-inf")

    # 一种只要不超过背包的限制即可
    # bag = [[0 for j in range(c + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):
            # 0表示该物体有任意件
            if s[i - 1] == 0:
                # 如果能够装下当前物体
                if j >= w[i - 1]:
                    # 此时价值应该等于放第当前物体，不放当前物体的价值中较大值
                    bag[i][j] = max(bag[i - 1][j], bag[i][j - w[i - 1]] + v[i - 1])
                # 装不下当前物体，最大价值就等于上一行的值
                else:
                    bag[i][j] = bag[i - 1][j]
            # 把有限件数都进行二进制分解，下面的问题就是01背包问题
            else:
                if j >= w[i - 1]:
                    # 此时价值应该等于放第当前物体，不放当前物体的价值中较大值
                    bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - w[i - 1]] + v[i - 1])
                # 装不下当前物体，最大价值就等于上一行的值
                else:
                    bag[i][j] = bag[i - 1][j]

    return bag


n = 6
c = 10
w = [2, 2, 3, 1, 5, 2]
v = [2, 3, 1, 5, 4, 3]
s = [1, 1, 1, 0, 1, 1]

print("混合背包问题价值矩阵为：")
bag_value = bag_max_value(n, c, w, v, s)
for v in bag_value:
    print(v)


# TODO 05.分组背包问题
def bag_max_value(n, c, w, v):
    """
       测试数据：
       n = 6  物品的的组数，
       c = 10 书包能承受的重量，
       w = [[2, 2], [2, 4], [3], [1], [5], [2]]  w分为几组，每组里面物体的重量和价值一一和v对应
       v = [[2, 3], [3, 7], [5], [5], [4], [3]]
       """

    # 要求恰好将背包装满的初始化如下：
    bag = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, len(bag[0])):
        bag[0][i] = float("-inf")

    # bag = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            for k in range(len(w[i - 1])):
                # 如果能够装下当前物体
                if j >= w[i - 1][k]:
                    # 此时价值应该等于放第当前物体，不放当前物体的价值中较大值
                    bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - w[i - 1][k]] + v[i - 1][k])
                # 装不下当前物体，最大价值就等于上一行的值
                else:
                    bag[i][j] = bag[i - 1][j]

    return bag


n = 6
c = 10
w = [[2, 2], [2, 4], [3], [1], [5], [2]]
v = [[2, 3], [3, 7], [5], [5], [4], [3]]
print("分组背包问题价值矩阵为：")
bag_value = bag_max_value(n, c, w, v)
for v in bag_value:
    print(v)

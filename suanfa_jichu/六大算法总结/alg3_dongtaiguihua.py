# 三、动态规划

# 能用动规解决的问题的特点 
# 能采用动态规划求解的问题的一般要具有3个性质：
#   (1) 最优化原理：如果问题的最优解所包含的子问题的解也是最优的，就称该问题具有最优子结构，即满足最优化原理。
#   (2) 无后效性：即某阶段状态一旦确定，就不受这个状态以后决策的影响。也就是说，某状态以后的过程不会影响以前的状态，只与当前状态有关。
#   (3)有重叠子问题：即子问题之间是不独立的，一个子问题在下一阶段决策中可能被多次使用到。（该性质并不是动态规划适用的必要条件，但是如果没有这条性质，动态规划算法同其他算法相比就不具备优势）

# 动规解题的一般思路   
# 动态规划所处理的问题是一个多阶段决策问题，一般由初始状态开始，通过对中间阶段决策的选择，达到结束状态。
# 这些决策形成了一个决策序列，同时确定了完成整个过程的一条活动路线(通常是求最优的活动路线)。
# 如下所示。动态规划的设计都有着一定的模式，一般要经历以下几个步骤：
#     初始状态→│决策１│→│决策２│→…→│决策ｎ│→结束状态

#     (1)划分阶段：按照问题的时间或空间特征，把问题分为若干个阶段。在划分阶段时，注意划分后的阶段一定要是有序的或者是可排序的，
#        否则问题就无法求解。
#     (2)确定状态和状态变量：将问题发展到各个阶段时所处于的各种客观情况用不同的状态表示出来。当然，状态的选择要满足无后效性。
#     (3)确定决策并写出状态转移方程：因为决策和状态转移有着天然的联系，状态转移就是根据上一阶段的状态和决策来导出本阶段的状态。
#        所以如果确定了决策，状态转移方程也就可写出。但事实上常常是反过来做，根据相邻两个阶段的状态之间的关系来确定决策方法和状态转移方程。
#     (4)寻找边界条件：给出的状态转移方程是一个递推式，需要一个递推的终止条件或边界条件。
#        一般，只要解决问题的阶段、状态和状态转移决策确定了，就可以写出状态转移方程（包括边界条件）。

# 实际应用中可以按以下几个简化的步骤进行设计：
#     （1）分析最优解的性质，并刻画其结构特征。
#     （2）递归的定义最优解。
#     （3）以自底向上或自顶向下的记忆化方式（备忘录法）计算出最优值
#     （4）根据计算最优值时得到的信息，构造问题的最优解


#  动态规划的主要难点在于理论上的设计，也就是上面4个步骤的确定，一旦设计完成，实现部分就会非常简单。
#
#      使用动态规划求解问题，最重要的就是确定动态规划三要素：
#     （1）问题的阶段
#     （2）每个阶段的状态
#     （3）从前一个阶段转化到后一个阶段之间的递推关系。
#
#      递推关系必须是从次小的问题开始到较大的问题之间的转化，从这个角度来说，动态规划往往可以用递归程序来实现，不过因为递推可以充分利用前面保存的子问题的解来减少重复计算，所以对于大规模问题来说，有递归不可比拟的优势，这也是动态规划算法的核心之处。
#
#     确定了动态规划的这三要素，整个求解过程就可以用一个最优决策表来描述，最优决策表是一个二维表，其中行表示决策的阶段，列表示问题状态，表格需要填写的数据一般对应此问题的在某个阶段某个状态下的最优值（如最短路径，最长公共子序列，最大价值等），填表的过程就是根据递推关系，从1行1列开始，以行或者列优先的顺序，依次填写表格，最后根据整个表格的数据通过简单的取舍或者运算求得问题的最优解。
#
#           f(n,m)=max{f(n-1,m), f(n-1,m-w[n])+P(n,m)}


# TODO 1.用动态解规划的思路求斐波那契数列
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    res = [0] * n
    res[0] = 1
    res[1] = 1

    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2]

    return res[-1]


# print(fibonacci(50000))


# TODO 2.数组最大不连续递增子序列
def max_monotonical_subsequence(li):
    length = len(li)

    res = [1] * length

    for i in range(1, length):
        for j in range(i):
            if li[i] > li[j] and res[j] + 1 > res[i]:
                res[i] = res[j] + 1

    res = max(res)

    return res


# li = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(max_monotonical_subsequence(li))


# TODO 3.数组最大连续子序列和
def max_subsequence_sum(li):
    length = len(li)

    max_sum = li[0]
    cur_sum = li[0]

    for i in range(1, length):
        cur_sum = max(li[i], cur_sum + li[i])

        if max_sum < cur_sum:
            max_sum = cur_sum

    return max_sum


# print(max_subsequence_sum([6, -1, 3, -4, -6, 9, 2, -2, 5]))


# TODO 4.数字塔从上到下所有路径中和最大的路径
# 数字塔是第i行有i个数字组成，从上往下每个数字只能走到他正下方数字或者正右方数字，求数字塔从上到下所有路径中和最大的路径，如有下数字塔
# 3
# 1    5
# 8    4    3
# 2    6    7    9
# 6    2    3    5    1

def nums_tower(li):
    h = len(li)

    # dp = [[0 for i in range(h)] for j in range(h)]
    # 其实只要保存一个一维数组就可以了，不断更新里面的值
    dp = [0 for i in range(h)]

    for i in range(h):
        for j in range(i + 1):
            if j == 0:
                dp[j] = dp[j] + li[i][j]
            elif j == i:
                dp[j] = dp[j - 1] + li[i][j]
            else:
                dp[j] = max(dp[j - 1], dp[j]) + li[i][j]

    return dp[-1]


# print(nums_tower([[3], [1, 5], [8, 4, 3], [2, 6, 7, 9], [6, 2, 3, 5, 1]]))


# TODO 5.两个字符串的最大公共子序列
# 比如字符串1：BDCABA；字符串2：ABCBDAB，则这两个字符串的最长公共子序列长度为4，最长公共子序列(不一定连续)是：BCBA
# 子串：按原顺序依次出现，禁止跳过某元素
# 子序列：在保持元素前后关系的前提下，可以跳过某些元素的序列
def lcs(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    c = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
    flag = [["0" for i in range(l2 + 1)] for j in range(l1 + 1)]

    for i in range(l1):
        for j in range(l2):
            if str1[i] == str2[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = "ok"
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = "left"
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = "right"

    return c, flag


def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'ok':
        printLcs(flag, a, i - 1, j - 1)
        print(a[i - 1], end='')
    elif flag[i][j] == 'left':
        printLcs(flag, a, i, j - 1)
    else:
        printLcs(flag, a, i - 1, j)


# a = 'BDCABA'
# b = 'ABCBDAB'
# c, flag = lcs(a, b)
# for i in c:
#     print(i)
# print('')
#
# for j in flag:
#     print(j)
# print('')
#
# printLcs(flag, a, len(a), len(b))


# TODO 6.背包问题
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
    bag = [[0 for j in range(c + 1)] for i in range(n + 1)]
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


# print("价值矩阵为：")
# bag_value = bag_max_value(n, c, w, v)
# # for v in bag_value:
# #     print(v)
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


# show(n, c, w, bag_value)


# TODO 7.找零钱问题
# 最少钱币找零问题：假设有1,2,5,10元的纸币，每种面额的纸币有无限张，给定需要找的零钱数目target，求最小的纸币数
def give_change(coins, target):
    m = len(coins)

    # 二维数组保存
    dp = [[0 for i in range(target + 1)] for j in range(m + 1)]
    for i in range(target + 1):
        dp[0][i] = target + 1

    for i in range(1, m + 1):
        for j in range(1, target + 1):
            if j >= coins[i - 1]:
                # j-conis[i-1], 剩下的金额需要的硬币数加1
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]
    return dp

    # # 一维数组保存
    # dp = [target + 1] * (target + 1)
    # dp[0] = 0
    # for i in range(1, m + 1):
    #     for j in range(1, target + 1):
    #         if j >= coins[i - 1]:
    #             dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
    #
    # return dp


coins = [1, 2, 5]
target = 10
dp = give_change(coins, target)
for d in dp:
    print(d)


# print(dp)
# [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3]

# 展示用了哪几种金额的纸币：
def show_used_coins(dp, coins):
    print('最少使用金币数为:', dp[-1][-1])
    x = [False for i in range(n)]
    j = c

    for i in range(len(coins), -1, -1):
        if dp[i][j] < dp[i - 1][j] and j > 0:
            x[i - 1] = True
            j = j % coins[i - 1]

    print('用到的硬币金额有:')
    for i in range(n):
        if x[i]:
            print(coins[i], '元', end=' ')


show_used_coins(dp, coins)


# TODO 8.取珠宝问题
# 一条直线上，有n 个房间，每个房间数量不等的财宝，
# 一个盗贼希望从房屋中盗取财宝，由于房屋有警报器，同时从相邻两个房间盗取珠宝就会触发警报，
# 求在不触发警报的情况下，最多可获取多少财宝？
def steal_jewellery(value):
    length = len(value)

    dp = [0 for i in range(length)]

    for i in range(length):
        # 状态转移方程
        dp[i] = max(dp[i - 2] + value[i], dp[i - 1])

    return dp


value = [1, 1, 1, 3, 1, 7]
# print(steal_jewellery(value))

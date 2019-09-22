# 面试题60：n个骰子的点数

# 将一个骰子投掷n次，获得的总点数为s，s的可能范围为n~6n。
# 掷出某一点数，可能有多种掷法，例如投掷2次，掷出3点，共有[1,2],[2,1]两种掷法。
# 请求出投掷n次，掷出n~6n点分别有多少种掷法。(除以总数就是出现的概率)


# 动态规划解法
class Solution(object):
    def numberOfDice(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n < 1:
            return

        # n个骰子的点数的和的最大值是6n, 最小值是n.
        # 初始化一个能够保存所有骰子不同点数和的二维数组.
        # 这里其实会浪费很多空间.
        dp = [[0 for i in range(6 * n)] for i in range(n)]

        # 设置第一个骰子的点数对应的出现次数
        for i in range(6):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(i, 6 * (i + 1)):

                # # 这里利用了python的切片性质, 下标为负值时是从后往前对应位置的值, 上面初始化为零了.
                # dp[i][j] = dp[i - 1][j - 6] + dp[i - 1][j - 5] + dp[i - 1][j - 4] + \
                #            dp[i - 1][j - 3] + dp[i - 1][j - 2] + dp[i - 1][j - 1]

                # 更简洁的写法, 计算量也会减少一部分
                for k in range(1, min(j + 1, 7)):
                    dp[i][j] += dp[i - 1][j - k]

        # dp记录了所有的中间值, 最后一个是掷n个骰子的情况
        count = dp[n - 1][n - 1:]

        return count


# 事实上只要保存两个时刻的值就可以了, 也即二维数组只要长度为2就可以了
class Solution2(object):
    def numberOfDice(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n < 1:
            return

        prob = [[0 for i in range(6 * n)] for i in range(2)]

        # 用来表示哪一个数组表示的是当前循环, 用它去计算下一个循环中的值.
        flag = 0

        for i in range(6):
            prob[flag][i] = 1

        for k in range(1, n):

            # 把用来记录后一个时刻的值的数组全部置0
            for i in range(6 * (k + 1)):
                prob[1 - flag][i] = 0

            for i in range(k, 6 * (k + 1)):
                # for j in range(1, 7):
                # 使用min函数来判断可以减少计算量
                for j in range(1, min(i + 1, 7)):
                    prob[1 - flag][i] += prob[flag][i - j]

            flag = 1 - flag

        return prob[flag][n - 1:]

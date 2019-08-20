# 面试题47：礼物的最大价值

# 在一个mxn的棋盘的每一格都有一个礼物，每个礼物都有一定的价值(价值大于0),
# 你可以从棋盘的左上角开始拿格子里的礼物，并且每次向左或向下移动一格，知道到达棋盘的右下角,
# 给定一个期盼及其上面的礼物，请计算你最多能拿到多少价值的礼物


class Solution1(object):
    def getMaxValue1(self, array):
        # 假设输入array为二维数组
        if not array or len(array) <= 0 or len(array[0]) <= 0:
            return 0

        rows = len(array)
        cols = len(array[0])

        maxValues = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    # 如果行号大于0，说明它上面有数字
                    up = maxValues[i - 1][j]
                if j > 0:
                    # 如果列号大于0，说明它左边有数字
                    left = maxValues[i][j - 1]

                maxValues[i][j] = max(up, left) + array[i][j]

        # return maxValues[-1][-1]
        return maxValues[rows - 1][cols - 1]


print("方法一")
s1 = Solution1()
print(s1.getMaxValue1([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s1.getMaxValue1([[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]))


# 优化一下, 不需要用到二维数组来保存所有格子的礼物价值
class Solution2:
    def getMaxValue1(self, array):
        # 假设输入array为二维数组
        if not array or len(array) <= 0 or len(array[0]) <= 0:
            return 0

        rows = len(array)
        cols = len(array[0])

        maxValues = [0 for i in range(cols)]

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    # 如果行号大于0，说明它上面有数字
                    up = maxValues[j]
                if j > 0:
                    # 如果列号大于0，说明它左边有数字
                    left = maxValues[j - 1]

                maxValues[j] = max(up, left) + array[i][j]

        return maxValues[-1]


print("方法二")
s1 = Solution2()
print(s1.getMaxValue1([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s1.getMaxValue1([[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]))


# 引申：求最小路径和(或者理解为最小的礼物价值)
class Solution3(object):
    def getMaxValue1(self, array):
        # 假设输入array为二维数组
        if not array or len(array) <= 0 or len(array[0]) <= 0:
            return 0

        rows = len(array)
        cols = len(array[0])

        minValues = [[0 for i in range(cols)] for j in range(rows)]

        # 与上面的不同之处主要就在于对第一行和第一列元素的处理
        # up和left初始化为0，min函数无法选出第一行和第一列的数据，因此要手动处理
        minValues[0][0] = array[0][0]
        for i in range(1, rows):
            minValues[i][0] = minValues[i - 1][0] + array[i][0]

        for j in range(1, cols):
            minValues[0][j] = minValues[0][j - 1] + array[0][j]

        for i in range(rows):
            for j in range(cols):
                if i != 0 and j != 0:
                    up = minValues[i - 1][j]
                    left = minValues[i][j - 1]

                    minValues[i][j] = min(up, left) + array[i][j]

        return minValues[rows - 1][cols - 1]


print("求最小礼物价值")
s2 = Solution3()
print(s2.getMaxValue1([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s2.getMaxValue1([[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]))

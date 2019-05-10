# 礼物的最大价值

class Solution1:
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

        return maxValues[rows - 1][cols - 1]


# s1 = Solution1()
# print(s1.getMaxValue1([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
# print(s1.getMaxValue1([[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]))


# 优化一下, 不需要用到二维数组;来保存所有格子的礼物价值
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

        return maxValues[cols - 1]


s1 = Solution2()
print(s1.getMaxValue1([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s1.getMaxValue1([[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]))


# 求最小路径和
class Solution3:
    def getMaxValue1(self, array):
        # 假设输入array为二维数组
        if not array or len(array) <= 0 or len(array[0]) <= 0:
            return 0

        rows = len(array)
        cols = len(array[0])

        minValues = [[0 for i in range(cols)] for j in range(rows)]

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

# s2 = Solution3()
# print(s2.getMaxValue1([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
# print(s2.getMaxValue1([[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]))

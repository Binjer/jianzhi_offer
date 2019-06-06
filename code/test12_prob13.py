# 面试题13：机器人的运动路径

# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
# 但是不能进入行坐标和列坐标的数位之和大于k的格子。

# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
# 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

# 本题同样考察回溯算法


class Solution(object):
    def movingCount(self, threshold, rows, cols):

        markMatrix = [False] * (rows * cols)
        count = self.movingCountCore(threshold, rows, cols, 0, 0, markMatrix)
        return count

    def movingCountCore(self, threshold, rows, cols, row, col, markMatrix):
        value = 0
        if self.check(threshold, rows, cols, row, col, markMatrix):
            markMatrix[row * cols + col] = True
            value = 1 + self.movingCountCore(threshold, rows, cols, row - 1, col, markMatrix) + \
                    self.movingCountCore(threshold, rows, cols, row + 1, col, markMatrix) + \
                    self.movingCountCore(threshold, rows, cols, row, col - 1, markMatrix) + \
                    self.movingCountCore(threshold, rows, cols, row, col + 1, markMatrix)
        return value

    def check(self, threshold, rows, cols, row, col, markMatrix):
        if row >= 0 and row < rows and col >= 0 and col < cols and \
                self.getDigitNum(row) + self.getDigitNum(col) <= threshold and not markMatrix[row * cols + col]:
            return True
        return False

    def getDigitNum(self, number):
        sum = 0
        while number > 0:
            sum += number % 10
            number = number // 10
        return sum

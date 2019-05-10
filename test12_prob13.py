# 机器人的运动路径

class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows < 1 or cols < 1:
            return 0
        markmatrix = [False] * (rows * cols)
        count = self.movingCountCore(threshold, rows, cols, 0, 0, markmatrix)
        return count

    def movingCountCore(self, threshold, rows, cols, row, col, markmatrix):
        value = 0
        if self.check(threshold, rows, cols, row, col, markmatrix):
            markmatrix[row * cols + col] = True
            value = 1 + self.movingCountCore(threshold, rows, cols, row - 1, col, markmatrix) + \
                    self.movingCountCore(threshold, rows, cols, row + 1, col, markmatrix) + \
                    self.movingCountCore(threshold, rows, cols, row, col - 1, markmatrix) + \
                    self.movingCountCore(threshold, rows, cols, row, col + 1, markmatrix)
        return value

    def check(self, threshold, rows, cols, row, col, markmatrix):
        if row >= 0 and row < rows and col >= 0 and col < cols and \
                self.getDigitNum(row) + self.getDigitNum(col) <= threshold and not markmatrix[row * cols + col]:
            return True
        return False

    def getDigitNum(self, number):
        sum = 0
        while (number > 0):
            sum += number % 10
            number = number // 10
        return sum

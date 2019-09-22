# 面试题29：顺时针打印矩阵

# 1  2  3  4
# 5  6  7  8
# 9 10 11 12
# 13 14 15 16
# 打印结果为1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10


# 这道题就是多个循环就可以解决的，因此要先把问题分析清楚，找到循环结束的条件(从外向内打印一圈接着一圈)
class Solution(object):
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code_with_name here
        if not matrix or len(matrix) <= 0 or len(matrix[0]) <= 0:
            print(matrix)
            return matrix

        r = len(matrix)
        c = len(matrix[0])
        res = []
        start = 0

        while r > 2 * start and c > 2 * start:
            self.printNum(matrix, r, c, start, res)
            start += 1
        print(res)
        return res

    def printNum(self, matrix, rows, columns, start, res):

        endX = columns - start - 1
        endY = rows - start - 1

        # 先从左往右打印一行
        for i in range(start, endX + 1):
            res.append(matrix[start][i])

        if start < endY:  # 需要第二步的前提是终止行数大于起始行数
            # 再从上往下打印一列
            for i in range(start + 1, endY + 1):
                res.append(matrix[i][endX])

        if start < endX and start < endY:  # 需要第三步的前提是终止行数大于其实行数，并且终止列数也大于起始列数
            # 再从右往左打印一行
            for i in range(endX - 1, -1 + start, -1):
                res.append(matrix[endY][i])

        if start < endX and start < endY - 1:  # 需要第四步的前提是终止行数比其实行数大2，并且终止列数大于起始列数
            # 再从上往下打印一列
            for i in range(endY - 1, start, -1):
                res.append(matrix[i][start])

        return res

    # 方法2: 矩阵旋转，每次取矩阵的第一行，任何逆时针旋转再取第一行
    def printMatrix2(self, matrix):
        # zip的妙用，适用于python2.x
        # return matrix and list(matrix.pop(0)) + self.printMatrix2(zip(*matrix)[::-1])

        # python3中zip是可迭代对象，因此要自己实现矩阵的转置
        res = []
        while matrix:
            res += matrix.pop(0)  # +=和append的区别在于后者会把一个列表中的所有元素当成一个元素追加
            if not matrix or not matrix[0]:
                break
            # (先对矩阵求转置，再上下翻转)==将矩阵逆时针旋转90度
            matrix = self.turn(matrix)
        return res

    def turn(self, matrix):
        """实现矩阵逆时针旋转90度"""

        row = len(matrix)
        col = len(matrix[0])
        newMatrix = []
        for i in range(col):
            temp = []
            for j in range(row):
                temp.append(matrix[j][i])  # 取矩阵的第j行第i列
            newMatrix.append(temp)
        newMatrix.reverse()  # 上下翻转

        return newMatrix


if __name__ == '__main__':
    s = Solution()
    s.printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    s.printMatrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    s.printMatrix([[1, 2, 3, 4]])
    s.printMatrix([[1], [2], [3], [4]])
    s.printMatrix([[1]])
    s.printMatrix([])

    res = s.printMatrix2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    res1 = s.printMatrix2([[1], [2], [3], [4]])
    print(res)
    print(res1)

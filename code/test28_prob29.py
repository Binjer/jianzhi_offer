# 顺时针打印矩阵

class Solution(object):
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
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

        if start < endY:
            # 再从上往下打印一列
            for i in range(start + 1, endY + 1):
                res.append(matrix[i][endX])

        if start < endX and start < endY:
            # 再从右往左打印一行
            for i in range(endX - 1, -1 + start, -1):
                res.append(matrix[endY][i])

        if start < endX and start < endY - 1:
            # 再从上往下打印一列
            for i in range(endY - 1, start, -1):
                res.append(matrix[i][start])

        return res

    # 方法2
    # python黑魔法
    def printMatrix2(self, matrix):
        return matrix and list(matrix.pop(0)) + self.printMatrix(zip(*matrix)[::-1])


s = Solution()
s.printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
s.printMatrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
s.printMatrix([[1, 2, 3, 4]])
s.printMatrix([[1], [2], [3], [4]])
s.printMatrix([[1]])
s.printMatrix([])

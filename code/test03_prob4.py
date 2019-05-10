# 二维数组中的查找
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 方法一: 双重循环遍历二维数组, 一一比较得出结论


# 方法二: 从右上角元素或者左下角元素开始比较
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m, n = len(array), len(array[0])
        row = 0
        col = n - 1
        while (row < m and col >= 0):
            if array[row][col] < target:
                row += 1
            elif array[row][col] > target:
                col -= 1
            else:
                return True
        return False

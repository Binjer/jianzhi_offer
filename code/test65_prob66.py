# 面试题66:构建乘积数组

# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
# 不能使用除法。


# 思路： 构建两个辅助数组
# [1,               A[0],            ...,    A[0]*A[1]*...A[n-3]          A[0]*A[1]*...A[n-2]]
# [A[n-1]*...A[1],  A[n-1]*...A[2],  ...,    A[n-1] ,                     1             ]
class Solution(object):
    def multiply(self, A):

        length = len(A)

        c = [1] * length
        d = [1] * length
        b = [1] * length

        for i in range(1, length):
            c[i] = c[i - 1] * A[i - 1]

        for j in range(length - 2, -1, -1):
            d[j] = d[j + 1] * A[j + 1]

        for k in range(length):
            b[k] = c[k] * d[k]

        return b


        # 代码可以再优化一下， 只用一个tmp保存d的临时值即可
        # b = [1] * length
        #
        # for i in range(1, length):
        #     b[i] = b[i - 1] * A[i - 1]
        #
        # tmp = 1
        # for j in range(length - 2, -1, -1):
        #     tmp *= A[j + 1]
        #     b[j] *= tmp
        #
        # return b

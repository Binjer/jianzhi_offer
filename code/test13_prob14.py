# 面试题14：剪绳子

# 给你一根长度为 n 绳子，请把绳子剪成 m 段（m、n 都是整数，n>1 并且 m>1）。
# 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]k[1] … k[m] 可能的最大乘积是多少？

# 例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到最大的乘积18。


class Solution(object):
    # 方法一：动态规划
    def MaxProductAfterCut1(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        products = [0] * (n+1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        for i in range(4, n + 1):
            max = 0
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                if product > max:
                    max = product
            products[i] = max
        print(products)
        return products[n]

    # 方法二：贪婪算法
    def MaxProductAfterCut2(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        timesOf3 = n // 3
        if n - 3 * timesOf3 == 1:
            timesOf3 -= 1

        timesOf2 = (n - 3 * timesOf3) // 2

        product = 3 ** timesOf3 * 2 ** timesOf2

        return product


if __name__ == "__main__":
    print(Solution().MaxProductAfterCut1(8))
    print(Solution().MaxProductAfterCut1(10))
    # print(Solution().NumberOf1(0))
    print(Solution().MaxProductAfterCut2(8))
    print(Solution().MaxProductAfterCut2(10))

# -*- coding:utf-8 -*-
class Solution:
    def MaxProductAfterCut(self, n):
        # 动态规划
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        products = [0] * (n + 1)
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

        return products[n]

    def MaxProductAfterCut2(self, n):
        # 贪婪算法
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
    print(Solution().MaxProductAfterCut(8))
    print(Solution().MaxProductAfterCut(10))
    # print(Solution().NumberOf1(0))
    print(Solution().MaxProductAfterCut2(8))
    print(Solution().MaxProductAfterCut2(10))

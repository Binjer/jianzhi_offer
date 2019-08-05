# 面试题42：连续子数组的最大和

# 思路一：分析规律:
# 1、定义两个变量，一个用来存储之前的累加值，一个用来存储当前的最大和。遍历数组中的每个元素，假设遍历到第i个数时：
# 　　①如果前面的累加值为负数或者等于0，那对累加值清0重新累加，把当前的第i个数的值赋给累加值。
# 　　②如果前面的累加值为正数，那么继续累加，即之前的累加值加上当前第i个数的值作为新的累加值。
# 2、初始化最大值为负无穷小或者数组的第一个值，判断累加值是否大于最大值：如果大于最大值，则最大值更新；否则，继续保留之前的最大和。


class Solution(object):
    def FindGreatestSumOfSubArray(self, array):

        if not array or len(array) <= 0:
            return 0

        curSum = 0
        greatestSum = float('-inf')
        for i in range(len(array)):
            if curSum <= 0:
                curSum = array[i]
            else:
                curSum += array[i]

            # 把临时的最大值保存下来
            if curSum > greatestSum:
                greatestSum = curSum

        return greatestSum


s = Solution()
print(s.FindGreatestSumOfSubArray([-1, -2, -3, -4, -5, -6]))


# 思路二：直接从动态规划的角度分析
# f(i) = array[i] ,           i=0或者f(i-1)<=0
#        f(i-1) + array[i],   i≠0并且f(i-1)>0
# 这里的f(i)就对应上面代码中的curSum, 我们通常基于递归来分析问题，但是最后会基于循环去编写代码

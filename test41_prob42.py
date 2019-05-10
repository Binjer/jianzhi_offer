# 连续子数组的最大和

# 分析规律或直接从动态规划的角度出发
class Solution1:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
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

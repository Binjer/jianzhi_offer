# 旋转数组的最小数字

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return
        if len(rotateArray) == 0:
            return 0

        index1 = 0
        index2 = len(rotateArray) - 1
        indexMid = index1

        while rotateArray[index1] >= rotateArray[index2]:

            if (index2 - index1) == 1:
                indexMid = index2
                break
            indexMid = (index1 + index2) // 2

            if rotateArray[indexMid] == rotateArray[index1] and rotateArray[index1] == rotateArray[index2]:
                low = rotateArray[index1]
                for i in range(index1 + 1, index2 + 1):
                    if rotateArray[i] < low:
                        low = rotateArray[i]
                return low

            if rotateArray[indexMid] >= rotateArray[index1]:
                index1 = indexMid

            if rotateArray[indexMid] <= rotateArray[index2]:
                index2 = indexMid

        return rotateArray[indexMid]


if __name__ == '__main__':
    s = Solution()
    print(s.minNumberInRotateArray([1, 2, 3, 4, 5]))
    print(s.minNumberInRotateArray([1, 1, 3, 4, 5]))
    print(s.minNumberInRotateArray([1, 1, 3, 4, 1]))
    print(s.minNumberInRotateArray([1]))
    print(s.minNumberInRotateArray([1, 0, 1, 1, 1]))

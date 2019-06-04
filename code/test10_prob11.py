# 面试题11: 旋转数组的最小数字

# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个升序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。

# 注意：数组可能包含重复项。
# 数组内所含元素非负，若数组大小为0，请返回-1。
class Solution(object):
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return
        if len(rotateArray) == 0:
            return 0

        # O(n)的常规解法
        # small = rotateArray[0]
        # for i in range(1, len(rotateArray)):
        #     if rotateArray[i] < small:
        #         small = rotateArray[i]

        # 二分查找的思路, 时间复杂度: O(logn)
        index1 = 0
        index2 = len(rotateArray) - 1
        indexMid = index1

        while rotateArray[index1] >= rotateArray[index2]:

            if (index2 - index1) == 1:
                indexMid = index2
                break
            indexMid = (index1 + index2) // 2

            if rotateArray[indexMid] == rotateArray[index1] and rotateArray[index1] == rotateArray[index2]:
                # 这种情况只能顺序查找
                low = rotateArray[index1]
                for i in range(index1 + 1, index2 + 1):
                    if rotateArray[i] < low:
                        low = rotateArray[i]
                return low

            # 此时最小元素在后半部分
            if rotateArray[indexMid] >= rotateArray[index1]:
                index1 = indexMid
            # 此时最小元素在前半部分
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
    print(s.minNumberInRotateArray([1, 1, 1, 0, 1]))

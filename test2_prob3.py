# 找出数组中重复的数字


class Solution1(object):
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here

        # 前面这两个判断是很重要的,保证了代码的鲁棒性
        if numbers is None or len(numbers) <= 1:
            return False
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return False

        # 方法一: 先排序, 然后遍历. 时间复杂度是O(nlogn+k)
        # numbers.sort()
        # for i in range(len(numbers) - 1):
        #     if numbers[i] == numbers[i + 1]:
        #         duplication[0] = numbers[i]
        #         return True
        # return False

        # 方法二: 利用哈希表: 时间复杂度是O(n), 空间复杂度是O(n)
        # used_dic = {}
        # used_dic = set()
        # for i in range(len(numbers)):
        #     if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
        #         return False
        #     if numbers[i] not in used_dic:
        #         used_dic[numbers[i]] = 1
        #     else:
        #         duplication[0] = numbers[i]
        #         return True

        # 方法三: 分析题干发现如果不存在重复的数字, 那么数组满足numbers[i] = i...
        # 每个数字最多只需要交换两次就能找到自己的位置O(2n)
        # 时间复杂度是O(n), 空间复杂度是O(1)
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    temp = numbers[i]
                    numbers[i] = numbers[temp]
                    numbers[temp] = temp

        return False


# 题目变形
# 不修改数组找出重复的数字
# 方法一: 复制一个长度为n+1的空间, 把原来数组的数字m复制到下标为m的位置, 如果某个位置已经有值了, 就找到了重复的数字
class Solution2:
    def duplicate1(self, numbers, duplication):

        if len(numbers) <= 0 or not numbers:
            return

        usedHashset = set()
        for i in range(len(numbers)):
            if numbers[i] not in usedHashset:
                usedHashset.add(numbers[i])
            else:
                duplication.insert(0, numbers[i])
                return True

    # 方法二
    # 二分查找: 对长度为n的数组需要查找logn次, 总的事件复杂度是nlogn
    def duplicate2(self, numbers):
        # write code here
        if not numbers or len(numbers) <= 0:
            return

        start = 1
        end = len(numbers) - 1
        count = 0

        while start <= end:
            middle = (end - start) // 2 + start

            for i in range(len(numbers)):
                if numbers[i] >= start and numbers[i] <= middle:
                    count += 1

            if end == start:
                if count == 0 and numbers[start] == numbers[end]:
                    return numbers[start]
                elif count >= 1:
                    return numbers[start]

            if count > middle - start + 1:
                end = middle
            else:
                start = middle + 1

        return False


# duplication = []
# print(Solution2().duplicate1([2, 3, 5, 4, 3, 2, 6, 7], duplication))
# print(duplication)

print(Solution2().duplicate2([2, 3, 5, 4, 3, 2, 6, 7]))
print(Solution2().duplicate2([3, 3, 2, 2]))

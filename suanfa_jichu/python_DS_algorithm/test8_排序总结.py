# 排序

# 1.冒泡排序
def bubbleSort(alist):
    for i in range(len(alist), 0, -1):
        for j in range(i - 1):
            if alist[j + 1] < alist[j]:
                alist[j + 1], alist[j] = alist[j], alist[j + 1]

    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]


# print(bubbleSort(alist))


def shortBubbleSort(alist):
    exchanges = True
    passNum = len(alist) - 1

    while passNum > 0 and exchanges:
        exchanges = False

        for i in range(passNum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

        passNum -= 1

    return alist


# print(shortBubbleSort(alist))


# 2.选择排序
def selectSort(alist):
    n = len(alist)

    # 每次选择最小的
    # for i in range(n - 1):
    #     min_index = i
    #     for j in range(i + 1, n):
    #         if alist[j] < alist[min_index]:
    #             min_index = j
    #     if min_index != i:
    #         alist[i], alist[min_index] = alist[min_index], alist[i]

    # 每次选择最大的, 这样结果会是降序的
    # for i in range(n - 1):
    #     max_index = i
    #     for j in range(i + 1, n):
    #         if alist[j] > alist[max_index]:
    #             max_index = j
    #     if max_index != i:
    #         alist[i], alist[max_index] = alist[max_index], alist[i]

    # 每次选择最大的与最后一位交换，这样最终结果还是升序的
    for i in range(n - 1, 0, -1):
        max_index = i
        for j in range(i+1):
            if alist[j] > alist[max_index]:
                max_index = j

            if max_index != i:
                alist[i], alist[max_index] = alist[max_index], alist[i]

    return alist


print("选择排序前", alist)
print("选择排序后", selectSort(alist))


# 3. 插入排序
def insertSort(alist):
    # for i in range(1, len(alist)):
    #
    #     currentvalue = alist[i]
    #     position = i
    #
    #     while position > 0 and alist[position - 1] > currentvalue:
    #         alist[position] = alist[position - 1]
    #         position -= 1
    #
    #     alist[position] = currentvalue

    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]

    return alist


# print(alist)
# print(insertSort(alist))

# 希尔排序
def shellSort(alist):
    n = len(alist)

    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]
            j = j - gap

        gap = gap // 2

    return alist


# print(shellSort(alist))


# 5. 归并排序
def merge_sort(alist):
    if len(alist) <= 1:  # 被分成两两一组或者单独一个元素时会return
        return alist

    # 二分分解
    num = len(alist) // 2
    lefthalf = merge_sort(alist[:num])
    # print(left)
    righthalf = merge_sort(alist[num:])
    # print(right)

    # '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    # left与right的下标指针
    # l, r = 0, 0
    # result = []
    # while l < len(left) and r < len(right):
    #     if left[l] < right[r]:
    #         result.append(left[l])
    #         l += 1
    #     else:
    #         result.append(right[r])
    #         r += 1
    # result += left[l:]
    # result += right[r:]
    # return result

    i = 0
    j = 0
    k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k] = lefthalf[i]
            i += 1
        else:
            alist[k] = righthalf[j]
            j += 1
        k += 1

    # 左边数组还未合并完
    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i += 1
        k += 1

    # 右边数组还未合并完
    while j < len(righthalf):
        alist[k] = righthalf[j]
        j += 1
        k += 1

    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print("归并排序前", alist)
print("归并排序后", merge_sort(alist))


# 6. 快速排序
def quickSort(alist, start, end):
    if start >= end:
        return

    # 设定起始元素为基准元素
    mid = alist[start]

    low = start
    high = end

    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    # 退出循环后,low与high重合,此时所指位置就是基准元素的正确位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quickSort(alist, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quickSort(alist, low + 1, end)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("快速排序前", alist)
quickSort(alist, 0, len(alist) - 1)
print("快速排序后", alist)


def qsort(L):
    if len(L) <= 1: return L
    return qsort([lt for lt in L[1:] if lt <= L[0]]) + L[0:1] + qsort([gt for gt in L[1:] if gt > L[0]])

# iList = [3, 14, 2, 12, 9, 33, 99, 35]
# # print(qsort(alist))
# print(qsort(iList))

def quick_sort(alist, left, right):
    if left < right:
        mid = (left + right) // 2
        sort_three(alist, left, mid, right)

        pivot = alist[right - 1]  # 基准元素取中间值
        low = left + 1
        high = right - 2

        while True:
            while alist[low] < pivot:
                low += 1

            while alist[high] > pivot:
                high -= 1

            if low < high:
                alist[low], alist[high] = alist[high], alist[low]
            else:
                break

        if low < right - 1:
            alist[low], alist[right - 1] = alist[right - 1], alist[low]

        quick_sort(alist, left, low - 1)
        quick_sort(alist, low + 1, right)

        return alist


def sort_three(alist, left, mid, right):
    """实现三个数的排序最简单的方法"""
    if alist[left] > alist[mid]:
        alist[left], alist[mid] = alist[mid], alist[left]

    if alist[mid] > alist[right]:
        alist[mid], alist[right] = alist[right], alist[mid]

    if alist[left] > alist[mid]:
        alist[left], alist[mid] = alist[mid], alist[left]

    # 排序完成后把中间的数放到最右边数的前一个位置上
    alist[mid], alist[right - 1] = alist[right - 1], alist[mid]

    return alist


# test_list = [54, 53, 56]
# print(sort_three(test_list, 0, 1, 2)) # 三个数排序测试

test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(quick_sort(test_list, 0, len(test_list) - 1))

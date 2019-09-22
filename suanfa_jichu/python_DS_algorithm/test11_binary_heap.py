# 二叉堆的实现

# from pythonds.trees.binheap import BinHeap
#
# bh = BinHeap()
# bh.insert(5)
# bh.insert(7)
# bh.insert(3)
# bh.insert(11)
#
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.isEmpty())


class BinaryHeap(object):
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    # 为插入子节点的数找到正确的位置,向上
    def perUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                tmp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heaplist.append(k)
        self.currentSize += 1
        self.perUp(self.currentSize)

    def perDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                # 交换父节点与子节点的数据
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    # 返回子树中较小的节点索引
    def minChild(self, i):
        # 这是没有右子树的情况
        if (i * 2 + 1) > self.currentSize:
            return i * 2
        # 这是右右子树的情况
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        # 记录根节点的值
        retval = self.heaplist[1]
        # 将最后一个节点的值赋给根节点
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize = self.currentSize - 1
        # 把原来最后一个节点的值弹出
        self.heaplist.pop()
        # 然后为根节点向下找到它合适的位置
        self.perDown(1)

        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.perDown(i)
            i = i - 1


bh = BinaryHeap()
bh.buildHeap([9, 5, 6, 2, 3])

print(bh.delMin())

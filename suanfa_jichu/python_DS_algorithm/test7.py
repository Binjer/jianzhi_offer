# 查找

# 1. 顺序查找
def sequentialSerach(alist, item):
    pos = 0
    found = False

    # for i in range(len(alist)):
    #     if alist[i] == item:
    #         found = True

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found


# print(sequentialSerach([1, 2, 3, 4, 5, 67, 8], 8))

# 有序列表的顺序查找
def orderSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1

    return found


# ali = [1, 3, 5, 7, 9, 11, 13, 15]


# 2. 二分查找: 适用于有序列表(或者先对列表进行排序)
def binarySearch(alist, item):
    first = 0
    last = alist[-1]
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


# 下面是递归版本
def binarySearch1(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearch1(alist[:midpoint], item)
            else:
                return binarySearch1(alist[midpoint + 1:], item)


# li3 = [1, 3, 5, 7, 9, 11, 13, 15]
# print(binarySearch1(li3, 5))


# 3. 哈希查找
def hashString(astring, tablesize):
    sum = 0
    for i in range(len(astring)):
        sum = sum + i * ord(astring[i])

    return sum % tablesize


# print(hashString("dog", 11))
# print(hashString("cat", 11))
# print(hashString("mycat", 11))


# 实现map抽象数据类型
class HashTable(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def put(self, key, data):
        hashvalue = self.hash_function(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def get(self, key):
        startslot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found =False
        position = startslot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

print(H.slots)
print(H.data)
print(H[20])
H[20] = "duck"
print(H.data)

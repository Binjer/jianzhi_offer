# 无序列表的实现: 链表.
class Node(object):
    """
    每个节点至少要保存两个信息: 数据字段和对下一个节点的引用;
    settter和getter方法是最常见的方法
    """

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


# temp = Node(93)
# print(temp.getData())
# print(temp.getNext())

class UnorderList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)  # 把新节点的next指向旧链表的head
        self.head = temp  # 把head指向新节点的数据

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            current = current.getNext()
            count += 1

        return count

    def search(self, item):
        current = self.head
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # 这说明要删除的元素是第一个
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


# mylist = UnorderList()
# print(mylist.isEmpty())
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)
# print(mylist.isEmpty())
# print(mylist.size())
# print(mylist.head.getData())
# print(mylist.search(17))
# mylist.remove(17)
# print(mylist.search(17))


# 有序列表
class OrderList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            current = current.getNext()
            count += 1

        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # 这说明要删除的元素是第一个
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


mylist1 = UnorderList()
print(mylist1.isEmpty())
mylist1.add(31)
mylist1.add(77)
# mylist1.add(17)
mylist1.add(93)
mylist1.add(26)
mylist1.add(54)
print(mylist1.isEmpty())
print(mylist1.size())
print(mylist1.head.getData())
print(mylist1.search(17))
mylist1.remove(17)
print(mylist1.search(17))

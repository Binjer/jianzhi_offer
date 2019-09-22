# 队列
# enqueue(), dequeue(), isempty(), size
# class Queue(object):
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def enqueue(self, item):
#         self.items.insert(0, item)
#
#     def dequeue(self):
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#
#
# q = Queue()
# print(q.isEmpty())
# q.enqueue(9)
# q.enqueue(8)
# q.enqueue(7)
# print(q.size())
# print(q.dequeue())

# 应用1: 烫手山芋问题
from pythonds.basic.queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(1, num):
            simqueue.enqueue(simqueue.dequeue())

        temp = simqueue.dequeue()
        print(temp + "*" * 10)

    return simqueue.dequeue()


# print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


# 应用2: 打印机等待时间模拟实验
import random


class Printer(object):
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task(object):
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getPages(self):
        return self.pages

    def getStamp(self):
        return self.timestamp

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def newPrintTask(object):
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask(object):
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("平均等待%6.2f secs, %3d tasks remaining" % (averageWait, printQueue.size()))


# for i in range(10):
#     simulation(3600, 10)

# 递归
from pythonds.basic.stack import Stack


def sumNum(num):
    if num == 0:
        return 0
    else:
        return num + sumNum(num - 1)


def sumNum1(num):
    if num == 100:
        return 100
    else:
        return num + sumNum1(num + 1)


# print(sumNum(10))
#
# print(sumNum1(0))

# 实现二进制到十六进制字符串的转换
# def toStr(n, base):
#     convertString = "0123456789ABCDEF"
#     if n < base:
#         return convertString[n]
#     else:
#         return toStr(n // base, base) + convertString[n % base]
#
#
# print(toStr(1453, 16))

def toStr(n, base):
    convertString = "01"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]


# print(toStr(2, 2))


# from pythonds.basic.stack import Stack
#
#
# def toStr(num, base):
#     s = Stack()
#     while num > 0:
#         rem = num % base
#         s.push(num % base)
#         num = num // base
#
#     newstr = ""
#     while not s.isEmpty():
#         newstr += str(s.pop())
#
#     return newstr
#
#
# print(toStr(8, 2))

def toStr2(num, base):
    s = Stack()
    convertString = "0123456789ABCDEF"

    while num > 0:
        if num < base:
            s.push(convertString[num])
        else:
            s.push(convertString[num % base])
        num = num // base

    res = ""
    while not s.isEmpty():
        res += str(s.pop())

    return res


# print(toStr2(1453, 16))

import turtle


# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()


def drawSpiral(myTurtle, linelen):
    if linelen > 0:
        myTurtle.forward(linelen)
        myTurtle.right(90)
        drawSpiral(myTurtle, linelen - 5)


# drawSpiral(myTurtle, 100)
# myWin.exitonclick()

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)


def test():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()


# test()


# 谢尔宾斯基三角形的绘制
def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree - 1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(myPoints, 3, myTurtle)
    myWin.exitonclick()


# main()

# 汉诺塔游戏

def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        print("moving disk from", fromPole, "to", toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


# def moveTower(n, a, b, c):
#     if n >= 1:
#         moveTower(n - 1, a, c, b)
#         print("moving disk from", a, "to", b)
#         moveTower(n - 1, c, b, a)


moveTower(3, 1, 2, 3)


# 应用2 动态规划

# 找零问题
def recMC(coinValueList, change):
    minCoins = change

    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)

            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


# 利用缓存减少重复计算
def recDC(coinValueList, change, knownResults):
    minCoins = change

    if change in coinValueList:
        knownResults[change] = 1
        return 1

    elif knownResults[change] > 0:
        return knownResults[change]

    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)

            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins

    return minCoins


# print(recMC([1, 5, 10, 25], 63))
# print(recDC([1, 5, 10, 25], 63, [0] * 64))


# 动态规划算法解决找零问题
def dpMakeChange(coinValueList, change, minCoins, coinUsed):
    for cents in range(1, change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin

    return minCoins[change]


def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


amnt = 78
clist = [1, 5, 10, 21, 25]
coinCount = [0] * (amnt + 1)
coinUsed = [0] * (amnt + 1)

print("Making change for", amnt, "requires")
print(dpMakeChange(clist, amnt, coinCount, coinUsed), "coins")
print("they are:")
printCoins(coinUsed, amnt)
print("the used list is as follows:")
print("coinUsed", coinUsed)
print("coinCount", coinCount)

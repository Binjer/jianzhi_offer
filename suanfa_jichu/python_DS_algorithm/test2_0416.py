# 栈的实现
# 应该有的方法isEmpty(), push(item), pop(), peek(), size()
# class Stack(object):
#     def __init__(self):
#         self.items = []
#
#     # isEmpty
#     def isEmpty(self):
#         return self.items == []
#
#     # 放入一个元素
#     def push(self, item):
#         self.items.append(item)
#
#     # 弹出栈顶的元素
#     def pop(self):
#         return self.items.pop()
#
#     # 从栈中返回顶部项, 但不删除它
#     def peek(self):
#         return self.items[-1]
#
#     def size(self):
#         return len(self.items)
#
#
# if __name__ == '__main__':
#     s = Stack()
#     print(s.isEmpty())
#     s.push(3)
#     s.push(4)
#     # print(s.pop())
#     print(s.isEmpty())
#     print(s.peek())
#     print(s.size())

from pythonds.basic.stack import Stack


# 栈的应用1: 解决括号是否匹配的问题
def parChcker(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        # if symbol == "(":
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


# print(parChcker("((()))())())(()"))
# print(parChcker("((())()()(()))"))
# print(parChcker("((())({[]}{}[][[[]]])()(()))"))


# 栈的应用2: 实现十进制数到二进制数的转换
# 简单修改就能实现十进制到指定进制的转换, 在函数参数中增加一个参数表示要转换的基数即可
def divideBy2(decNumber, base=2):
    remstack = Stack()

    while decNumber > 0:
        # rem = decNumber % 2
        rem = decNumber % base
        remstack.push(rem)
        # decNumber = decNumber // 2
        decNumber = decNumber // base

    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString


print(divideBy2(3))


# print(divideBy2(25))
# print(divideBy2(25, 16))


# 栈的应用3: 中缀表达式转后缀表达式
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        # 如果标记是操作数,将其附加到列表的结尾
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        # 如果标记是左括号,将其压入栈中
        elif token == "(":
            opStack.push(token)
        # 如果标记是右括号, 要弹出栈中的运算符, 直到遇到左括号为止, 并把弹出的运算符加到列表最后
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        # 如果是+ - * /运算符, 将其压入栈中之前, 要先判断有没有比它运算等级更先或相等的运算符, 有的话要先把这些加到输出列表结尾
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


# 栈的应用4: 后缀表达式计算
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def postfixEval(postfixExpr):
    opStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            opStack.push(int(token))
        else:
            operand2 = opStack.pop()
            operand1 = opStack.pop()
            result = doMath(token, operand1, operand2)
            opStack.push(result)

    return opStack.pop()


print(postfixEval("7 8 + 3 2 + /"))

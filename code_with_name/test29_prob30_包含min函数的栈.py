# 面试题30：包含最小元素的栈
# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。
# 要求在该栈中，调用min、push及pop的时间复杂度都是O(1)

# 思路分析:
# 增加一个辅助栈, 用于存放不同时刻的栈的最小元素.
# 当在栈中添加第一个元素时, 辅助栈中也添加这个元素(一定为最小值)
# 当在栈中添加第二个元素时, 如果元素的值比辅助栈中存放的值小, 就把这个值也加入到辅助栈中, 反之, 将辅助栈中存放的最小值再加入到栈中一次.
# 弹出元素时, 栈和辅助栈同时弹出.
# 这样就保证了辅助栈中的栈顶元素始终是栈中的最小元素.


class Solution(object):
    def __init__(self):
        self.s1 = []
        # 最小元素栈
        self.s2 = []

    def push(self, node):
        self.s1.append(node)
        if len(self.s2) == 0 or node < self.min():
            self.s2.append(node)
        else:
            self.s2.append(self.min())

    def pop(self):
        return self.s1.pop() and self.s2.pop()

    def top(self):
        return self.s1[-1]

    def min(self):
        return self.s2[-1]

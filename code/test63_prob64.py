# 求1+2+3+...+n
# 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）

class Solution:
    def Sum_Solution12(self, n):
        # write code here

        # 解法一:　sum函数
        # return sum(list(range(1, n+1)))

        # 解法二：　使用递归，　用逻辑与运算来作为递归的终止条件
        return n and n + self.Sum_Solution(n - 1)

    # 解法三：　利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况．
    # 如果对n连续进行两次反运算，那么非零的n转换为True，0转换为False。利用这一特性终止递归
    def Sum_Solution3(self, n):
        # write code here
        return self.sum(n)

    def sum0(self, n):
        return 0

    def sum(self, n):
        func = {False: self.sum0, True: self.sum}
        return n + func[not not n](n - 1)

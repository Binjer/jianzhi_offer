# 面试题27：二叉树的镜像


# 递归解法
class Solution1(object):
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return root

        # 先前序遍历树的每个节点----根, 左, 右
        # 交换左右节点
        temp = root.left
        root.left = root.right
        root.right = temp

        # 递归交换左子树中的左右节点
        if root.left:
            self.Mirror(root.left)

        # 递归交换右子树中的左右节点
        if root.right:
            self.Mirror(root.right)

        return root


# 循环解法
# 可利用栈来完成
class Solution2(object):
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return

        stack1 = []
        stack1.append(root)

        while len(stack1) > 0:
            par = stack1.pop()

            temp = par.left
            par.left = par.right
            par.right = temp

            if par.left:
                stack1.append(par.left)

            if par.right:
                stack1.append(par.right)

        return root

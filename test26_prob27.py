# 二叉树的镜像

# 递归解法
class Solution(object):
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return

        # 这个判断不是必须的吗? 应该判断一下比较合适
        if root.left is None and root.right is None:
            return

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


# 循环解法, 借助栈或者双向队列完成后进先出的功能
class Solution2(object):
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return

        q = []
        q.append(root)

        while len(q) > 0:
            par = q.pop()

            temp = par.left
            par.left = par.right
            par.right = temp

            if par.left:
                q.append(par.left)

            if par.right:
                q.append(par.right)

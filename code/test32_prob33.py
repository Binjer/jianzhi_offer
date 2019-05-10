# 二叉搜索树的后序遍历
# 二叉搜索(排序)树: 如果左子树不为空, 那么左子树上的点都比根节点小; 右子树不为空, 右子树上的点都比根节点大
# 左右子树也都是二叉搜索树


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if not sequence or length <= 0:
            return False

        root = sequence[-1]

        # 先找到序列中第一个比根节点大的数的位置, 就找到了左子树和右子树
        # 注意python中的切片是左闭右开
        i = 0
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1

        # 如果右子树中有比根节点小的数, 就返回False
        for node in sequence[i:-1]:
            if node < root:
                return False
            i += 1

        # 然后递归的判断左子树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])

        # 递归的判断右子树
        right = True
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:-2])

        return left and right

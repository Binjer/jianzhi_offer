# 面试题33：二叉搜索树的后序遍历


# 名字解释--二叉搜索(排序)树: 如果左子树不为空, 那么左子树上的点都比根节点小; 右子树不为空, 右子树上的点都比根节点大
# 左右子树也都是二叉搜索树

# 后序遍历序列中最后一个值是根节点的值，左子树的值都比根节点小，右子树的值都比根节点大，这样可以找到左右子树；
# 递归可以找到子树的左右子树


class Solution(object):
    def VerifySquenceOfBST(self, sequence):

        # 常规判断思路
        # length = len(sequence)
        # if not sequence or length <= 0:
        #     return False
        #
        # root_val = sequence[-1]
        #
        # i = 0
        # while i < length - 1:
        #     if sequence[i] > root_val:
        #         break
        #     i += 1
        #
        # for j in range(i, length - 1):
        #     if sequence[j] < root_val:
        #         return False

        length = len(sequence)
        if not sequence or length <= 0:
            return False

        root_val = sequence[-1]

        # 先找到序列中第一个比根节点大的数的位置, 就找到了左子树和右子树
        # 注意python中的切片是左闭右开
        i = 0
        for node_val in sequence[:-1]:
            if node_val > root_val:
                break
            i += 1

        # 如果右子树中有比根节点小的数, 就返回False
        for node_val in sequence[i:-1]:
            if node_val < root_val:
                return False
            i += 1

        # 然后递归的判断左子树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])

        # 递归的判断右子树
        right = True
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])

        return left and right

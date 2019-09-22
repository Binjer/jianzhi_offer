# b站算法题目：
# 1.假设现在需要对一串字符串进行解码：1→A...26→Z，输入数字N，问有多少种输出的可能（如：输入111，输出3）
# 动态规划

# 2.图像P(h,w)，像素值[0,255]，卷积核K(m,m)矩阵，元素值为[0,1.]的浮点数。
# 输出后图像大小为O(h-m+1,w-m+1),h>=m,w>=m,给了卷积后图O的元素之计算公式，要求将图片按行输出。
# 卷积的实现

# 3.将一句话中，字母数是奇数个的单词翻转。


def reverse_odd_str(str1):
    str1_li = str1.split(" ")

    res = []
    for s in str1_li:
        if len(s) % 2 == 1:
            res.append(s[::-1])
        else:
            res.append(s)

    res = " ".join(res)

    return res


# print(reverse_odd_str("i am a veryd happy student"))


# 借助numpy实现卷积
import numpy as np


def conv_forward(z, K, b, padding=(0, 0), strides=(1, 1)):
    """
    多通道卷积前向过程
    :param z: 卷积层矩阵,形状(N,C,H,W)，N为batch_size，C为通道数
    :param K: 卷积核,形状(C,D,k1,k2), C为输入通道数，D为输出通道数
    :param b: 偏置,形状(D,)
    :param padding: padding
    :param strides: 步长
    :return: 卷积结果
    """
    padding_z = np.lib.pad(z, ((0, 0), (0, 0), (padding[0], padding[0]), (padding[1], padding[1])), 'constant',
                           constant_values=0)
    N, _, height, width = padding_z.shape
    C, D, k1, k2 = K.shape
    assert (height - k1) % strides[0] == 0, '步长不为1时，步长必须刚好能够被整除'
    assert (width - k2) % strides[1] == 0, '步长不为1时，步长必须刚好能够被整除'

    # 初始化输出的feature map
    conv_z = np.zeros((N, D, 1 + (height - k1) // strides[0], 1 + (width - k2) // strides[1]))

    for n in np.arange(N):
        for d in np.arange(D):
            for h in np.arange(height - k1 + 1)[::strides[0]]:
                for w in np.arange(width - k2 + 1)[::strides[1]]:
                    conv_z[n, d, h // strides[0], w // strides[1]] = np.sum(
                        padding_z[n, :, h:h + k1, w:w + k2] * K[:, d]) + b[d]

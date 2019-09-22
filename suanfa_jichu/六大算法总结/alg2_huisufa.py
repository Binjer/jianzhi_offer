# 二、回溯法


# 回溯法是一种试探性算法，从这一点上看，它很像穷举法。
# 回溯法是有组织的进行穷举，在试探过程中不断通过题设要求减少搜索空间，
# 而这种减少不是一个一个解的减少，而是对搜索空间进行大规模剪枝，
# 从而使得实际搜索空间远远小于问题的解空间，所以回溯法的实际运行效率还是比较高的。

# 搜索策略：要用回溯法解决问题，那首先要确定问题的状态空间树。
# 这个并不是很难，就看每一步选择有多少个可选值就可以了，
# 第一步有8个可选值，那树第一层就有8个节点，第二步有5个可选值，那第一层每个节点都有5个分支，则第二层有8×5=40个节点，
# 以此类推……到第n层一共有m1×m2×……×mn个节点，其中mi为第i步的可选值的个数。


# 用回溯法解题一般思想为：
# （1）在解空间树中，从根节点出发，采用深度优先搜索的思想来遍历解空间树。
#     每一次遍历节点时都判断当前 节点是否为合法解，如果为合法解，那么继续遍历其自子树，
#     如果不是合法节点，那么访问其下一个兄弟节点，
#     如果没有下一个兄就退回到父节点（回溯），访问父节点下一个兄弟节点。
# （2）回溯法结束的条件是回溯到根节点而且所有子树均已遍历到。
# （3）回溯法归根结底是一种带有节点判断条件的深度优先搜索算法。

# 回溯法解题一般步骤：
# （1）针对所给问题，确定问题的解空间：首先应明确定义问题的解空间，问题的解空间应至少包含问题的一个（最优）解。
# （2）确定结点的扩展搜索规则
# （3）以深度优先方式搜索解空间，并在搜索过程中用剪枝函数避免无效搜索。


# 1.八皇后问题
def eight_queens(num, state=()):
    # 找到了一个可行解
    if num - 1 == len(state):
        for i in range(num):
            if not conflict(state, i):
                yield (i,)
    else:
        for pos in range(num):  # 如果冲突则遍历其兄弟节点
            if not conflict(state, pos):
                # 如果不冲突则继续遍历其子节点
                for res in eight_queens(num, state + (pos,)):
                    yield (pos,) + res


def conflict(state, pos):
    nextY = len(state)
    if pos in state:
        return True

    for i in range(nextY):
        # 行列坐标的差相等，说明在一条斜率为负的斜线上
        if nextY - pos == i - state[i]:
            return True

        if nextY + pos == i + state[i]:
            return True

    return False


# 打印出每一种结果和总数
print("所有可行的摆放方式如下：")
for i in list(eight_queens(8)):
    print(i)
print("一共有%d种摆法" % len(list(eight_queens(8))))


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


print("一种摆放方式如下, X代表棋子：")
prettyprint(list(eight_queens(8))[0])

# 2.图的m-着色问题
'''图的m着色问题'''

# 用邻接表表示图
n = 5  # 节点数
a, b, c, d, e = range(n)  # 节点名称
# 列表的下标表示起始顶点，依次是a，b，c，d，e
# 字典的key表示到达顶点，值表示边的权重
graph = [
    {b, c, d},
    {a, c, d, e},
    {a, b, d},
    {a, b, c, e},
    {b, d}
]

m = 4  # m种颜色

x = [0] * n  # 一个解（n元数组，长度固定）注意：解x的下标就是a,b,c,d,e!!!
X = []  # 一组解


# 冲突检测
def conflict(k):
    global n, graph, x

    # 找出第k个节点前面已经涂色的邻接节点
    nodes = [node for node in range(k) if node in graph[k]]
    if x[k] in [x[node] for node in nodes]:  # 已经有相邻节点涂了这种颜色
        return True

    return False  # 无冲突


# 图的m着色（全部解）
def dfs(k):  # 到达（解x的）第k个节点
    global n, m, graph, x, X

    if k == n:  # 解的长度超出
        print(x)
        # X.append(x[:])
    else:
        for color in range(m):  # 遍历节点k的可涂颜色编号（状态空间），全都一样
            x[k] = color
            if not conflict(k):  # 剪枝
                dfs(k + 1)


# 测试
print("着色问题的方案：")
dfs(a)  # 从节点a开始


# 3.全排列问题
def permutation(ss, start, end):
    if start == end:
        ss = list(map(str, ss))
        ss = "".join(ss)
        res.append(ss)
    else:
        for i in range(start, end + 1):
            # 有重复字符时，剪枝，但这种思路还是不完整，因此最后用set去重比较好
            if ss[i] == ss[start] and start != i:
                continue
            
            ss[start], ss[i] = ss[i], ss[start]
            permutation(ss, start + 1, end)
            ss[start], ss[i] = ss[i], ss[start]


res = []
a = [1, 2, 3, 4, 1]
permutation(a, 0, len(a) - 1)
print(len(res))
print(len(list(set(res))))

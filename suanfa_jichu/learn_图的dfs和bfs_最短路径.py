# 4 5 1 4
# 10 20 30 40
# 1 2 2
# 1 3 3
# 2 3 2
# 3 4 3
# 4 3 3

# n个顶点，m条边，s代表出发顶点，d代表到达顶点
n, m, s, d = 4, 5, 1, 4
road = [[1, 2, 2], [1, 3, 3], [2, 3, 2], [3, 4, 3], [4, 3, 3]]

graph = {i: {} for i in range(1, n + 1)}
# i表示出发顶点，j表示到达顶点，w表示边的权重
for i, j, w in road:
    graph[i].update({j: w})

print("构建的图为：", graph)


def find_all_path(graph, start, end, path=[]):
    path = path + [start]  # 这里是重新创建了一个参数
    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_path(graph, node, end, path)
            for newpath in new_paths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]  # 这里是重新创建了一个参数
    if start == end:
        return path

    if start not in graph:
        return None

    shortest_path = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path

    return shortest_path


paths = find_all_path(graph, s, d)
shortest_path = find_shortest_path(graph, s, d)
print("从%d到%d所有的路径为:%s" % (s, d, paths))
print("从%d到%d最短的路径为:%s" % (s, d, shortest_path))


def bfsTravel(graph, start):
    # 前驱节点
    frontiers = [start]
    # 遍历过的节点
    travel = [start]

    # 当前驱节点为空时停止遍历
    while frontiers:
        # 当前层的节点，相比frontiers是下一层
        nexts = []
        for f in frontiers:
            # 对当前层的所有节点(graph[f]表示节点f可以直接到达的所有节点的字典)
            for cur in graph[f]:
                if cur not in travel:
                    travel.append(cur)  # 没有访问过则入队
                    nexts.append(cur)  # 保存当前节点作为前驱节点

        frontiers = nexts

    return travel


travel_bfs = bfsTravel(graph, s)
print("从%d节点bfs遍历的结果为%s" % (s, travel_bfs))


def dfsTravel(graph, start):
    travel = []  # 存放访问过的节点的列表
    stack = [start]  # 构造一个堆栈

    while stack:
        cur = stack.pop()
        if cur not in travel:
            travel.append(cur)

        for nxt in graph[cur]:
            if nxt not in travel:
                stack.append(nxt)

    return travel


travel_dfs = dfsTravel(graph, s)
print("从%d节点bfs遍历的结果为%s" % (s, travel_dfs))

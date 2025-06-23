from collections import deque
from typing import List


# 拓扑排序（保证无环）
class TopologicalSort:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

    def topologicalSort(self) -> List:
        # 入度数组
        in_degree = [0] * self.n
        # 邻接表
        edge_lists = [[] for _ in range(self.n)]
        for edge in self.edges:
            edge_lists[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1

        # 使用双端队列作为队列
        queue = deque()
        # 将所有入度为0的节点加入队列
        for i in range(self.n):
            if in_degree[i] == 0:
                queue.append(i)

        result = []
        while queue:
            v = queue.popleft()
            result.append(v)
            # 遍历当前节点的所有邻接节点
            for u in edge_lists[v]:
                in_degree[u] -= 1
                if in_degree[u] == 0:
                    queue.append(u)

        return result

# 最短路

## Reference

- https://leetcode.cn/discuss/post/01LUak/


## 单源最短路：Dijkstra 算法

Dijkstra 算法是一种用于计算带权有向图或无向图中单个源节点到其他所有节点的最短路径的贪心算法


```python
import heapq


def dijkstra(graph, start):
    # 初始化距离字典，存储从起始节点到各个节点的最短距离
    distances = {node: float('inf') for node in graph}
    # 起始节点到自身的距离为 0
    distances[start] = 0
    # 优先队列，存储 (距离, 节点) 元组
    priority_queue = [(0, start)]

    while priority_queue:
        # 从优先队列中取出距离最小的节点
        current_distance, current_node = heapq.heappop(priority_queue)

        # 如果当前距离大于已记录的最短距离，跳过
        if current_distance > distances[current_node]:
            continue

        # 遍历当前节点的所有邻居节点
        for neighbor, weight in graph[current_node].items():
            # 计算从起始节点经过当前节点到邻居节点的距离
            distance = current_distance + weight

            # 如果新的距离小于已记录的最短距离，更新距离并加入优先队列
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# 示例图的邻接表表示
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 起始节点
start_node = 'A'

# 调用 Dijkstra 算法
shortest_distances = dijkstra(graph, start_node)

# 输出结果
for node, distance in shortest_distances.items():
    print(f"从节点 {start_node} 到节点 {node} 的最短距离是: {distance}")
```

## 全源最短路：Floyd 算法

Floyd-Warshall 算法（通常简称为 Floyd 算法）是一种用于求解图中所有节点对之间最短路径的算法，它可以处理有向图和无向图，并且允许图中存在负权边，但不能存在负权环.


```python
INF = float('inf')


def floyd(graph):
    # 获取图中所有的节点
    nodes = list(graph.keys())
    num_nodes = len(nodes)
    # 初始化距离矩阵
    dist = {node: {neighbor: INF for neighbor in nodes} for node in nodes}
    # 填充初始距离
    for node in nodes:
        dist[node][node] = 0
        for neighbor, weight in graph[node].items():
            dist[node][neighbor] = weight

    # 三重循环更新距离矩阵
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# 示例图用字典表示
graph = {
    'A': {'B': 5, 'D': 10},
    'B': {'C': 3},
    'C': {'D': 1},
    'D': {}
}

# 调用 Floyd 算法
shortest_distances = floyd(graph)

# 输出结果
for start_node in shortest_distances:
    for end_node in shortest_distances[start_node]:
        if shortest_distances[start_node][end_node] == INF:
            print(f"从节点 {start_node} 到节点 {end_node} 的最短距离: 无穷大")
        else:
            print(f"从节点 {start_node} 到节点 {end_node} 的最短距离: {shortest_distances[start_node][end_node]}")
    
```
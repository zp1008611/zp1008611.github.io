# DFS和BFS

## Reference

- https://leetcode.cn/discuss/post/3581143/fen-xiang-gun-ti-dan-tu-lun-suan-fa-dfsb-qyux/
- https://leetcode.cn/discuss/post/3580195/fen-xiang-gun-ti-dan-wang-ge-tu-dfsbfszo-l3pa/
- https://leetcode.cn/discuss/post/3580195/fen-xiang-gun-ti-dan-wang-ge-tu-dfsbfszo-l3pa/

**DFS与BFS的实现方式：**

```
from collections import deque

def dfs_recursive(graph, start):
    """DFS递归实现"""
    visited = set()
    result = []
    
    def dfs_helper(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph.get(node, []):
                dfs_helper(neighbor)
    
    dfs_helper(start)
    return result

def dfs_iterative(graph, start):
    """DFS迭代实现（使用栈）"""
    if start not in graph:
        return []
    
    visited = set()
    result = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # 注意：栈是后进先出，因此邻居节点需要逆序入栈
            for neighbor in reversed(graph.get(node, [])):
                stack.append(neighbor)
    
    return result

def bfs(graph, start):
    """BFS实现（使用队列）"""
    if start not in graph:
        return []
    
    visited = set()
    result = []
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# 示例图结构
example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 使用示例
print("DFS (Recursive) starting from 'A':", dfs_recursive(example_graph, 'A'))
print("DFS (Iterative) starting from 'A':", dfs_iterative(example_graph, 'A'))
print("BFS starting from 'A':", bfs(example_graph, 'A'))
```

**DFS找环：**

```python
def has_cycle(graph):
    visited = set()
    
    for node in graph:
        if node not in visited:
            stack = [(node, False)]  # (节点, 是否已处理所有邻接节点)
            recursion_stack = set()
            
            while stack:
                current, processed = stack.pop()
                
                if processed:
                    # 回溯：移除当前节点的递归路径标记
                    recursion_stack.remove(current)
                    continue
                
                if current in recursion_stack:
                    return True
                
                # 标记当前节点为已访问并加入递归栈
                visited.add(current)
                recursion_stack.add(current)
                
                # 将当前节点重新压入栈，并标记为已处理
                stack.append((current, True))
                
                # 将所有邻接节点压入栈（按逆序，确保正序处理）
                for neighbor in reversed(graph[current]):
                    if neighbor not in visited:
                        stack.append((neighbor, False))
                    elif neighbor in recursion_stack:
                        return True
    
    return False
```




## DFS

> 找连通块、判断是否有环
> DFS：找来一个栈，把起点入栈，出栈访问，若出栈点还没访问，访问出栈点，并把逆序邻居入栈（邻居入栈要写在if访问判断内，否则写在外面的话，已经访问过的节点的邻居又入栈，会造成死循环）
> 起点入栈->循环：（出栈->没访问过的出栈的邻居逆序入栈）
> 注意邻居入栈是要写出栈点是否被访问的if判断内

1. 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。返回矩阵中 省份 的数量。[LC547](https://leetcode.cn/problems/number-of-provinces/description/) [x]

    - 从点i=0开始DFS，arr记录遍历的点，DFS断了之后就是一个省份，从未访问的点中剔除arr的点（做差集），arr清空，继续找点做DFS

2. 有一个具有 n 个顶点的 双向 图，其中每个顶点标记从 0 到 n - 1（包含 0 和 n - 1）。图中的边用一个二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示顶点 ui 和顶点 vi 之间的双向边。 每个顶点对由 最多一条 边连接，并且没有顶点存在与自身相连的边。请你确定是否存在从顶点 source 开始，到顶点 destination 结束的 有效路径 。给你数组 edges 和整数 n、source 和 destination，如果从 source 到 destination 存在 有效路径 ，则返回 true，否则返回 false 。[LC1971](https://leetcode.cn/problems/find-if-path-exists-in-graph/description/) [x]

    - 从source开始DFS，记录遍历的点，如果destination在遍历的点中，则为True


3. 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）。graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。[LC797所有可能路径](https://leetcode.cn/problems/all-paths-from-source-to-target/description/)

    - 


4. 有 n 个房间，房间按从 0 到 n - 1 编号。最初，除 0 号房间外的其余所有房间都被锁住。你的目标是进入所有的房间。然而，你不能在没有获得钥匙的时候进入锁住的房间。当你进入一个房间，你可能会在里面找到一套 不同的钥匙，每把钥匙上都有对应的房间号，即表示钥匙可以打开的房间。你可以拿上所有钥匙去解锁其他房间。给你一个数组 rooms 其中 rooms[i] 是你进入 i 号房间可以获得的钥匙集合。如果能进入 所有 房间返回 true，否则返回 false。[LC841](https://leetcode.cn/problems/keys-and-rooms/description/)

5. 给你一个整数 n ，表示一张 无向图 中有 n 个节点，编号为 0 到 n - 1 。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。请你返回无法互相到达的不同点对数目。[LC2316](https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/)


6. 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 [LC1319](https://leetcode.cn/problems/number-of-operations-to-make-network-connected/description/)


7. 给你一个正整数 n ，表示总共有 n 个城市，城市从 1 到 n 编号。给你一个二维数组 roads ，其中 roads[i] = [ai, bi, distancei] 表示城市 ai 和 bi 之间有一条 双向 道路，道路距离为 distancei 。城市构成的图不一定是连通的。两个城市之间一条路径的 分数 定义为这条路径中道路的 最小 距离。城市 1 和城市 n 之间的所有路径的 最小 分数。注意：一条路径指的是两个城市之间的道路序列。一条路径可以 多次 包含同一条道路，你也可以沿着路径多次到达城市 1 和城市 n 。测试数据保证城市 1 和城市n 之间 至少 有一条路径。

8. 你正在维护一个项目，该项目有 n 个方法，编号从 0 到 n - 1。给你两个整数 n 和 k，以及一个二维整数数组 invocations，其中 invocations[i] = [ai, bi] 表示方法 ai 调用了方法 bi。已知如果方法 k 存在一个已知的 bug。那么方法 k 以及它直接或间接调用的任何方法都被视为 可疑方法 ，我们需要从项目中移除这些方法。只有当一组方法没有被这组之外的任何方法调用时，这组方法才能被移除。返回一个数组，包含移除所有 可疑方法 后剩下的所有方法。你可以以任意顺序返回答案。如果无法移除 所有 可疑方法，则 不 移除任何方法。[LC3310](https://leetcode.cn/problems/remove-methods-from-project/description/)

9. 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。[LC207](https://leetcode.cn/problems/course-schedule/description/)


## 网格图DFS

> 要注意网格图的x，y坐标表示，假设m=len(grid),n=len(grid[0])，那么x的范围为0-n，y的范围为0-m

1. 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。[LC200岛屿数量](https://leetcode.cn/problems/number-of-islands/description/) [x]

    - 遍历grid[0][0]找到第一个陆地点，对陆地点做dfs，邻居为上下左右旁边为‘1’的点，grid中遍历过的点记为‘0’，dfs每断一次，岛屿数量+1
    - 网格图m，n特判，特判m=1，n=1

2. 给你一个大小为 m x n 的二进制矩阵 grid 。岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。岛屿的面积是岛上值为 1 的单元格的数目。计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。[LC695](https://leetcode.cn/problems/max-area-of-island/description/)

3. 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。[LC面试题16.19](https://leetcode.cn/problems/pond-sizes-lcci/description/)


## BFS

> 求最短路

1. 给你一个整数 n 和一个二维整数数组 queries。有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。[LC3243](https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/description/)

2. 有 n 个人，每个人都有一个  0 到 n-1 的唯一 id 。给你数组 watchedVideos  和 friends ，其中 watchedVideos[i]  和 friends[i] 分别表示 id = i 的人观看过的视频列表和他的好友列表。Level 1 的视频包含所有你好友观看过的视频，level 2 的视频包含所有你好友的好友观看过的视频，以此类推。一般的，Level 为 k 的视频包含所有从你出发，最短距离为 k 的好友观看过的视频。给定你的 id  和一个 level 值，请你找出所有指定 level 的视频，并将它们按观看频率升序返回。如果有频率相同的视频，请将它们按字母顺序从小到大排列。[LC1311](https://leetcode.cn/problems/get-watched-videos-by-your-friends/description/)


## 网格BFS

1. 给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始），矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）。同时给你迷宫的入口 entrance ，用 entrance = [entrancerow, entrancecol] 表示你一开始所在格子的行和列。每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 entrance 最近 的出口。出口 的含义是 maze 边界 上的 空格子。entrance 格子 不算 出口。请你返回从 entrance 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 -1 。[LC1926](https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/description/)

2. 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：路径途经的所有单元格的值都是 0 。路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。畅通路径的长度 是该路径途经的单元格总数。[LC1091](https://leetcode.cn/problems/shortest-path-in-binary-matrix/description/)

3. 你现在手里有一份大小为 n x n 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地。请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的，并返回该距离。如果网格上只有陆地或者海洋，请返回 -1。我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。[LC1162](https://leetcode.cn/problems/as-far-from-land-as-possible/description/)

## 拓扑排序

1. 
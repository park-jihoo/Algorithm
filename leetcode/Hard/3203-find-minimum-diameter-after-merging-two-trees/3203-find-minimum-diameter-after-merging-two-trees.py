class Tree:
    def __init__(self, edges: List[List[int]], num_nodes: int):
        self.edges = edges
        self.num_nodes = num_nodes
        self.graph = self.build_graph()
        self.diameter = None
        self.center = None

    def build_graph(self) -> defaultdict:
        graph = defaultdict(list)
        for u, v in self.edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def bfs(self, start: int) -> Tuple[int, List[int]]:
        dist = [-1] * self.num_nodes
        dist[start] = 0
        q = deque([start])
        farthest_node = start

        while q:
            node = q.popleft()
            for neighbor in self.graph[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    farthest_node = neighbor
                    q.append(neighbor)

        return farthest_node, dist

    def calculate_diameter_and_center(self):
        farthest, _ = self.bfs(0)
        other_end, dist = self.bfs(farthest)
        self.diameter = max(dist)
        self.center = [
            i
            for i, d in enumerate(dist)
            if d == self.diameter // 2 or d == (self.diameter + 1) // 2
        ]

    def get_diameter(self) -> int:
        if self.diameter is None:
            self.calculate_diameter_and_center()
        return self.diameter

    def get_center(self) -> List[int]:
        if self.center is None:
            self.calculate_diameter_and_center()
        return self.center


class Solution:
    # 그래프 2개의 중심을 연결하여 diameter을 구하기
    # 중심은 어떻게 구하는데? -> 모든 점에서 점까지의 길이를 구해야 할듯
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        tree1 = Tree(edges1, len(edges1) + 1)
        tree2 = Tree(edges2, len(edges2) + 1)

        diameter1 = tree1.get_diameter()
        diameter2 = tree2.get_diameter()

        return max(
            diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1
        )

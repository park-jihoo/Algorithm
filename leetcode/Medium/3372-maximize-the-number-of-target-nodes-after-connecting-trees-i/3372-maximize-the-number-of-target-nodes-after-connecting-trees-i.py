class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        answers = self.find_ans(edges1, k)
        sec_tree = max(self.find_ans(edges2, k-1))
        return [ans + sec_tree for ans in answers]

    def find_ans(self, edges, k):
        n = len(edges) + 1
        answers = [0] * n
        if k < 0:
            return answers
        graph = [[] for _ in range(n)]
        for edge1, edge2 in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
        for i in range(n):
            answers[i] = self.depth_first(graph, i, k, -1)
        return answers

    def depth_first(self, graph, node, k, prev):
        res = 1
        if k == 0:
            return res
        for cur_node in graph[node]:
            if cur_node != prev:
                res += self.depth_first(graph, cur_node, k-1, node)
        return res
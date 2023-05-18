class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {x : [] for x in range(n)}
        reach = {x : [] for x in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            reach[edge[1]].append(edge[0])
        #unreachable nodes
        unreachable = [x for x in range(n) if len(reach[x]) == 0]
        return unreachable
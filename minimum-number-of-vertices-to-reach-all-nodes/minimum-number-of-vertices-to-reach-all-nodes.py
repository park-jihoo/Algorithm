class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reach = {x : [] for x in range(n)}
        for edge in edges:
            reach[edge[1]].append(edge[0])
        #unreachable nodes
        unreachable = [x for x in range(n) if len(reach[x]) == 0]
        return unreachable
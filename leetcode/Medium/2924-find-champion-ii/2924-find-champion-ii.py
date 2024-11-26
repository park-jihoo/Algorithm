class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s,e in edges:
            graph[e].append(s)
        ans = [x for x in range(n) if len(graph[x]) == 0]
        if len(ans) != 1:
            return -1
        else:
            return ans[0]
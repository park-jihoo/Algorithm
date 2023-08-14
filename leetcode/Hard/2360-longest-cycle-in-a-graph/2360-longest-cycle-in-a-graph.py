class Solution:
    def dfs(self, i, edges):
        global visited, stack, start, answer, dfsvisited
        visited[i] = True
        if edges[i] == -1:
            dfsvisited = []
        elif not visited[edges[i]]:
            dfsvisited.append(edges[i])
            self.dfs(edges[i], edges)
        elif edges[i] in dfsvisited:
            answer = max(answer, len(dfsvisited) - dfsvisited.index(edges[i]))
        stack.append(i)
        pass

    def longestCycle(self, edges: List[int]) -> int:
        global visited, stack, start, answer, dfsvisited
        visited = [False for i in range(len(edges))]
        stack = []
        answer = -1
        for i in range(len(edges)):
            if visited[i] == False:
                start = i
                dfsvisited = [i]
                self.dfs(i, edges)

        return answer

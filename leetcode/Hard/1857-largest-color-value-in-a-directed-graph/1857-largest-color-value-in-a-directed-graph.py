class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = {x: [] for x in range(n)}
        deg = [0 for _ in range(n)]
        flag = 0
        answer = 0
        count = [[0]*26 for _ in range(n)]
        for s, e in edges:
            graph[s].append(e)
            deg[e] += 1
            if s == e:
                return -1
        q = deque([])
        for idx, d in enumerate(deg):
            if d == 0:
                q.append(idx)

        while q:
            s = q.popleft()
            flag += 1
            order = ord(colors[s]) - ord('a')
            count[s][order]+=1
            answer = max(answer, count[s][order])
            for e in graph[s]:
                for i in range(26):
                    count[e][i] = max(count[e][i], count[s][i])
                deg[e] -= 1
                if deg[e] == 0:
                    q.append(e)
        if flag == n:
            return answer
        return -1
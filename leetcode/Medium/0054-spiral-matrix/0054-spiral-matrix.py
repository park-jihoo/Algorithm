class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        answer = []
        now = (0, 0)
        nowd = 0
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(len(matrix))]
        for i in range(m * n):
            answer.append(matrix[now[0]][now[1]])
            visited[now[0]][now[1]] = True
            if not 0 <= now[0] + d[nowd][0] < m or not 0 <= now[1] + d[nowd][1] < n:
                nowd = (nowd + 1) % 4
            elif visited[now[0] + d[nowd][0]][now[1] + d[nowd][1]]:
                nowd = (nowd + 1) % 4
            now = (now[0] + d[nowd][0], now[1] + d[nowd][1])
        return answer

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        waters = deque([])
        answer = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    waters.append((i, j))
                    answer[i][j] = 0
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while waters:
            x, y = waters.popleft()
            for dx, dy in d:
                if 0<=x+dx<m and 0<=y+dy<n and answer[x+dx][y+dy] == -1:
                    answer[x+dx][y+dy] = answer[x][y] + 1
                    waters.append((x+dx, y+dy))
        return answer
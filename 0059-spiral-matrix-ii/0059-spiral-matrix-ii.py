class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[0]*n for _ in range(n)]
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, k = 0, 0, 0
        for i in range(n*n):
            answer[x][y] = i+1
            if not 0 <= x+d[k][0] < n or not 0<=y+d[k][1] <n:
                k = (k+1)%4
            elif answer[x+d[k][0]][y+d[k][1]] != 0:
                k = (k+1)%4
            x, y = x+d[k][0], y+d[k][1]
        return answer
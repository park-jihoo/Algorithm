class Solution:
    def d(self, x):
        return 1-x
    def matrixScore(self, grid: List[List[int]]) -> int:
        # 제일 왼쪽이 0 아닌거부터 해서 row로 바꾸고, col의 경우는 다수인 경우로 둠
        for idx, row in enumerate(grid):
            if row[0] == 0:
                grid[idx] = list(map(self.d, row))
        a = 1
        ans = 0
        for col in range(len(grid[0])-1, -1, -1):
            score = sum([grid[x][col] for x in range(len(grid))])
            ans += a * max(score, len(grid) - score)
            a *= 2
        return ans
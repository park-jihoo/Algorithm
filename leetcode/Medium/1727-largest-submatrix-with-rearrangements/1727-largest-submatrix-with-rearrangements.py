class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        height = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            order_height = sorted(height)
            for j in range(n):
                ans = max(ans, order_height[j]*(n-j))
        return ans
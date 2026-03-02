class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxRight = [0 for _ in range(n)]
        for idx, row in enumerate(grid):
            for i in range(len(row)-1, -1, -1):
                if row[i] == 1:
                    maxRight[idx] = i
                    break

        swaps = 0
        for i in range(n):
            j = i
            while j < n and maxRight[j] > i:
                j += 1
            if j == n:
                return -1
            while j > i:
                maxRight[j], maxRight[j-1] = maxRight[j-1], maxRight[j]
                swaps += 1
                j -= 1
        return swaps
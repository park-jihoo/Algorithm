class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        idx = len(grid[0]) - 1
        answer = 0
        for row in grid:
            start, end = 0, idx
            while start < end:
                mid = (start + end) // 2
                if row[mid] < 0:
                    end = mid
                else:
                    start = mid + 1
            if row[start] < 0:
                answer += (len(grid[0]) - start)
                idx = start
        return answer
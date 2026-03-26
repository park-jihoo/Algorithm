class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(A):
            seen = set()
            top = 0
            for i, r in enumerate(A):
                seen |= set(r)
                top += sum(r)
                bot = total - top
                if top - bot in [0, A[0][0],  A[0][-1], A[i][0]]: return True
                if len(A[0]) > 1 and i > 0 and top - bot in seen: return True
            return False
        
        total = sum(sum(r) for r in grid)
        if check(grid) or check(grid[::-1]): return True
        grid = list(zip(*grid))
        return check(grid) or check(grid[::-1])
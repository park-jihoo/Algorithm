class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xmm, ymm, ans = {}, {}, 0
        for x, y in buildings:
            if x not in xmm:
                xmm[x] = [y, y]
            else:
                xmm[x][0] = min(xmm[x][0], y)
                xmm[x][1] = max(xmm[x][1], y)
            if y not in ymm:
                ymm[y] = [x, x]
            else:
                ymm[y][0] = min(ymm[y][0], x)
                ymm[y][1] = max(ymm[y][1], x)
        for x, y in buildings:
            if y not in xmm[x] and x not in ymm[y]:
                ans += 1
        return ans

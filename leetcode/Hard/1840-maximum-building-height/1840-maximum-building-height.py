class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        l = len(restrictions)

        def yCap(x1, y1, x2, y2):
            return min(y2, y1 + abs(x2 - x1))

        def yPeak(x1, y1, x2, y2):
            return (y1 + y2 + x2 - x1) >> 1

        for i in range(1, l):
            restrictions[i][1] = yCap(*restrictions[i - 1], *restrictions[i])

        for i in range(l - 2, -1, -1):
            restrictions[i][1] = yCap(*restrictions[i + 1], *restrictions[i])

        ans = 0
        for i in range(1, l):
            ans = max(ans, yPeak(*restrictions[i - 1], *restrictions[i]))

        return max(ans, restrictions[-1][1] + n - restrictions[-1][0])

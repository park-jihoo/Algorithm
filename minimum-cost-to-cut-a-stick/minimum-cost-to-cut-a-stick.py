class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        #array dp sort
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        cost = [[0]*m for _ in range(m)]

        for k in range(2, m):
            for i in range(m):
                j = i + k
                if j >= m:
                    continue
                cost[i][j] = cuts[j] - cuts[i] + min(cost[i][s] + cost[s][j] for s in range(i+1, j))
        return cost[0][m-1]
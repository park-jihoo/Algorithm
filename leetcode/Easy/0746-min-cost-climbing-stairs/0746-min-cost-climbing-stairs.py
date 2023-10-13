class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        p1, p2 = cost[1], cost[0]
        for i in range(2, n):
            temp = cost[i] + min(p1, p2)
            p2 = p1
            p1 = temp
        return min(p1, p2)
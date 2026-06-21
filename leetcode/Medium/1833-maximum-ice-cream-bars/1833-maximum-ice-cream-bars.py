class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        while ans < len(costs) and coins >= costs[ans]:
            coins -= costs[ans]
            ans += 1
        return ans

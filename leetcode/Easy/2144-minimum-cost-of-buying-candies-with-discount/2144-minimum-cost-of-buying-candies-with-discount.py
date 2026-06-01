class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        return sum(x for idx, x in enumerate(cost) if (len(cost) - idx)%3 )
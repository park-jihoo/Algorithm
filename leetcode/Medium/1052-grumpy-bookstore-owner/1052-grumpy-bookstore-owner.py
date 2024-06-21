class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cur = sum(customers[x] for x in range(len(customers)) if grumpy[x] == 0 or x < minutes)
        ans = cur
        for i in range(len(customers) - minutes):
            cur += grumpy[i+minutes] * customers[i + minutes] - grumpy[i] * customers[i]
            ans = max(cur, ans)
        return ans
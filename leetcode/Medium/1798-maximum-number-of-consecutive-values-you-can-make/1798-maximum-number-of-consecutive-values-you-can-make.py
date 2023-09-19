class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # Array Greedy
        ans = 1
        for a in sorted(coins):
            if a > ans:
                break
            ans += a
        return ans

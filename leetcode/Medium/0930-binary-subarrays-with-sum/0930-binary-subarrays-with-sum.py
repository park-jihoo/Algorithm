class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        cur = 0
        freq = {}

        for num in nums:
            cur += num
            if cur == goal:
                ans += 1
            if cur - goal in freq:
                ans += freq[cur - goal]
            freq[cur] = freq.get(cur, 0) + 1
        return ans
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        for i in range(n):
            seen, cnt= 0, 0
            for x in nums[i:]:
                cnt += ((seen >> x) & 1) == 0
                seen |= (1<<x)
                ans += cnt * cnt
        return ans
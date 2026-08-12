
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans, left = 0, -1
        cnt = Counter()
        for right, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k:
                left += 1
                cnt[nums[left]] -= 1
            ans = max(ans, right-left)
        return ans
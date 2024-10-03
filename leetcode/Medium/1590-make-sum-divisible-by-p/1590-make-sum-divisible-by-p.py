class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        r = sum(nums) % p
        if r == 0:
            return 0
        psum = 0
        ans = len(nums)
        idx_map = {0: -1}
        for idx, val in enumerate(nums):
            psum = (psum + val) % p
            if (psum - r) % p in idx_map:
                ans = min(ans, idx - idx_map[(psum - r) % p])
            idx_map[psum] = idx
        return ans if ans < len(nums) else -1

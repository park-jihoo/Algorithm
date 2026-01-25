class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1]
        if k == 1:
            return 0
        for i in range(len(nums)-k+1):
            ans = min(ans, nums[i+k-1] - nums[i])
        return ans
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        minval = nums[0]
        for i in range(1, len(nums)):
            if minval + k < nums[i]:
                minval = nums[i]
                ans += 1
        return ans + 1

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            for j in range(i+1, len(nums) - 1):
                x = bisect_left(nums, nums[i]+nums[j], j+1)
                ans += (x - (j+1))

        return ans
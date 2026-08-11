class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n, seen = len(nums), set(nums)
        ans = nums[0]

        for i in range(1, n):
            if nums[i] == nums[i-1]+1:
                ans += nums[i]
            else:
                break
        
        while ans in seen:
            ans += 1
        return ans
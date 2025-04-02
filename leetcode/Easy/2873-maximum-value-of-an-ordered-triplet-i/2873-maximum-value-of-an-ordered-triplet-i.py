class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        for k in range(2, len(nums)):
            for j in range(k):
                for i in range(j):
                    ans = max(ans, (nums[i] - nums[j])* nums[k] )
        return ans
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mv, ans, streak = 0, 0, 0
        for num in nums:
            if mv < num:
                mv = num
                ans, streak = 0, 1
            elif mv == num:
                streak += 1
            else:
                streak = 0
            ans = max(ans, streak)
        return ans

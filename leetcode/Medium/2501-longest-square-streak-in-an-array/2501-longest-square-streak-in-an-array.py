class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        streak = 0
        set_nums = set(nums)
        for start in nums:
            curr_streak, curr = 0, start
            while curr in set_nums:
                curr_streak += 1
                if curr**2 > 10**5:
                    break
                curr *= curr
            streak = max(streak, curr_streak)
        return streak if streak >= 2 else -1

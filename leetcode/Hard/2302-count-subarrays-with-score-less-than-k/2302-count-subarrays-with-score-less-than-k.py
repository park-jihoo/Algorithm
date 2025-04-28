class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        p = [0] + list(accumulate(nums))
        left, ans = 0, 0
        for right in range(1, len(nums) + 1):
            scr = (p[right] - p[left]) * (right - left)
            while scr >= k and left < right:
                left += 1
                scr = (p[right] - p[left]) * (right - left)
            ans += (right - left)
        return ans
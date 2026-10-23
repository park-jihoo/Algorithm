class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = (1 << len(nums)) - 1
        cnt = 0
        for idx, val in enumerate(nums):
            if idx != val:
                ans &= val
            else:
                cnt += 1
        return 0 if cnt == len(nums) else ans

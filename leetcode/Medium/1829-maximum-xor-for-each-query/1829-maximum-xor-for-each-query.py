class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        pref = [0] * n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i-1]^nums[i]
        mask = (1 << maximumBit) - 1
        ans = [0] * n

        for i in range(n):
            curr = pref[n - i - 1]
            ans[i] = curr ^ mask
        return ans
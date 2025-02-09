class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = len(nums) * (len(nums)-1) // 2
        numi = Counter([val-idx for idx, val in enumerate(nums)])
        for key, val in numi.items():
            ans -= (val * (val-1) // 2)
        return ans
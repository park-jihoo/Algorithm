class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = []
        for idx, n in enumerate(nums):
            ans.append(nums[(idx + n) % len(nums)])
        return ans

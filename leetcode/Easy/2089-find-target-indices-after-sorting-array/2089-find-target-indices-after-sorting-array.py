class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans = []
        nums.sort()
        for idx in range(len(nums)):
            if nums[idx] == target:
                ans.append(idx)
        return ans
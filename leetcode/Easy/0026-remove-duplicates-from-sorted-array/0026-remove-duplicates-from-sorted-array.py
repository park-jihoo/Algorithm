class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        nums.clear()
        nums.extend(list(s))
        nums.sort()
        return len(nums)
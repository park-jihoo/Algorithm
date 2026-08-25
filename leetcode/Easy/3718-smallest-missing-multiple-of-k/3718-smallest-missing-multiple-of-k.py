class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        sets = set(range(k, (len(nums)+1)*k + 1, k)) 
        return min(sets - set(nums))
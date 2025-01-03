class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref = list(accumulate(nums))
        last = pref.pop()
        return sum(1 if x >= last / 2 else 0 for x in pref)
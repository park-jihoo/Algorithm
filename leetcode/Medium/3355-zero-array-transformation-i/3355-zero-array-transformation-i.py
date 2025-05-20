class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0]*(len(nums))
        for s, e in queries:
            diff[s] += 1
            if e+1 < len(diff):
                diff[e+1] -= 1
        return all(x <= y  for x, y in zip(nums, list(accumulate(diff))))
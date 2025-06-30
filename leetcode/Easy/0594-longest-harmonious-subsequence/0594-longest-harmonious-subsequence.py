class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        ans = 0
        if max(nums) == min(nums):
            return 0
        for val in cntr.keys():
            if cntr[val] and cntr[val+1]:
                ans = max(ans, cntr[val] + cntr[val+1])
        return ans if ans != 1 else 0
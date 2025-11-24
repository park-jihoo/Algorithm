class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans, cur = [], 0
        for i in nums:
            cur = (cur*2+i)%5
            ans.append(cur==0)
        return ans
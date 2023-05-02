class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        if len([x for x in nums if x<0])%2 == 1:
            return -1
        else:
            return 1
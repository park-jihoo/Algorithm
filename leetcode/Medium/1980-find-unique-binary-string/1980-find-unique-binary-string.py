class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        intnums = set([int(x, 2) for x in nums])
        setnums = set(range(n+1))
        remain = bin(list(setnums - intnums)[0])[2:]
        return "0"*(n-len(remain))+remain
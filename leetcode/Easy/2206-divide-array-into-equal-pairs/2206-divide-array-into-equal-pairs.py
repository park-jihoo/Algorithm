class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(val%2==0 for key, val in Counter(nums).items())
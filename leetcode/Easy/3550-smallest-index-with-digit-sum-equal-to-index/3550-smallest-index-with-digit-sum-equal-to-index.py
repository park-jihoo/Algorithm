class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == sum(int(digit) for digit in str(nums[i])):
                return i
        return -1

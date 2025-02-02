class Solution:
    def check(self, nums: List[int]) -> bool:
        minus = int(nums[0] < nums[-1])
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                minus += 1
            if minus > 1:
                return False
        return True

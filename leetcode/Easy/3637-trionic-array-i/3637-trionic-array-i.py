class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        changes = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return False
            elif nums[i] > nums[i+1]:
                if i == 0:
                    return False
                if changes and changes[-1] != i-1:
                    return False
                if i + 1 == len(nums) - 1:
                    return False
                changes.append(i)
        return len(changes) > 0
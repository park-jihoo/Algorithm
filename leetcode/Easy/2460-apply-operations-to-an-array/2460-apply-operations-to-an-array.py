class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n, z = len(nums), 0
        ans = []
        for i in range(n - 1):
            if nums[i] == 0:
                z += 1
            elif nums[i] == nums[i + 1]:
                ans.append(nums[i] * 2)
                nums[i + 1] = 0
            else:
                ans.append(nums[i])
        ans.append(nums[-1])
        return ans + [0] * z

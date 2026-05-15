class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < ans:
                ans = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        return ans

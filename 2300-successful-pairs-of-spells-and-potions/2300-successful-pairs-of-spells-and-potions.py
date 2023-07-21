class Solution:
    def length(self, nums, x):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= x:
                right = mid - 1
            else:
                left = mid + 1
        return len(nums) - left

    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions = sorted(potions)
        answer = []
        for spell in spells:
            suc = success / spell
            answer.append(self.length(potions, suc))
        return answer

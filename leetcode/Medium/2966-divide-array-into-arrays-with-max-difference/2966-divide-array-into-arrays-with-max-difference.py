class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = [
            [nums[3 * i], nums[3 * i + 1], nums[3 * i + 2]]
            for i in range(len(nums) // 3)
        ]
        for elems in ans:
            if elems[2] - elems[0] > k:
                return []
        return ans

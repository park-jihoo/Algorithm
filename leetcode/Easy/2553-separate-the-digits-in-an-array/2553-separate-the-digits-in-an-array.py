class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.extend(map(int, list(str(num))))
        return ans

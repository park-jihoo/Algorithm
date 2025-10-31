class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(2)]

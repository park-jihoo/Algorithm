class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        original = set(range(1, len(nums)+1))
        duplicate = Counter(nums).most_common()[0][0]
        loss = list(original - set(nums))[0]
        return [duplicate, loss]
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numset = set(nums)
        numCounter = Counter(nums)
        return [numCounter.most_common()[0][0], list(set(range(1, len(nums)+1)) - numset)[0]]
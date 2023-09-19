from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common()[0][0]

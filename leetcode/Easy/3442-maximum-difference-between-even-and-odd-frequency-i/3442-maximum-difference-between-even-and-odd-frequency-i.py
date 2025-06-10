class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [x for x in Counter(s).values()]
        odd = [x for x in freq if x % 2 == 1]
        even = [x for x in freq if x % 2 == 0]
        return max(odd)-min(even)
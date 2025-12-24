class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        pref = list(accumulate(sorted(capacity, reverse=True)))
        return bisect_left(pref, sum(apple)) + 1

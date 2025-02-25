class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        pref = [0] + list(accumulate(arr))
        ans = 0
        odd = sum(x%2 for x in pref)
        even = len(pref) - odd
        return (odd * even) % (10**9 + 7)
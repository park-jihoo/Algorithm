class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans, n = [], len(nums)
        odd_diff = [(nums[i+1] - nums[i]) % 2 != 0 for i in range(n - 1)]
        pref = list(accumulate(odd_diff, initial=0))
        for s, e in queries:
            odds = pref[e] - pref[s]
            ans.append(odds == (e-s))
        return ans
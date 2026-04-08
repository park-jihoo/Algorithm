class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9+7
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                tmp = nums[idx]
                nums[idx] = (tmp*v)%mod
                idx+=k
        ans = 0
        for n in nums:
            ans^=n
        return ans
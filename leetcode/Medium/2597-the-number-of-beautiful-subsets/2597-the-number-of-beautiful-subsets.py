class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        cnt = [Counter() for i in range(k)]
        for n in nums:
            cnt[n%k][n] += 1
        res = 1
        for i in range(k):
            prev, dp0, dp1 = 0, 1 ,0
            for a in sorted(cnt[i]):
                v = 2 ** (cnt[i][a])
                if prev + k  == a:
                    dp0, dp1 = dp0+dp1, dp0*(v-1)
                else:
                    dp0, dp1 = dp0+dp1, (dp0+dp1)*(v-1)
                prev = a
            res *= dp0 + dp1
        return res-1
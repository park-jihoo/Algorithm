class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        MOD = 1000000007
        BASE = 911382323

        n = len(nums)
        h = [0] * (n + 1)
        p = [0] * (n + 1)
        p[0] = 1

        # Compute prefix hashes and powers of BASE
        for i in range(n):
            h[i + 1] = (h[i] * BASE + nums[i]) % MOD
            p[i + 1] = p[i] * BASE % MOD

        def check(length):
            cnt = {}
            for l in range(n - length + 1):
                r = l + length
                key = (h[r] - h[l] * p[length] % MOD + MOD) % MOD
                cnt[key] = cnt.get(key, 0) + 1

            for times in cnt.values():
                if times == 1:
                    return True
            return False

        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
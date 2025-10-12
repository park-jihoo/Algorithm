class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9+7
        @lru_cache(None)
        def dp(_m, _k, i, flag):
            if _m < 0 or _k < 0 or _m + flag.bit_count() < _k:
                return 0
            if _m == 0:
                return 1 if _k == flag.bit_count() else 0    
            if i >= len(nums):
                return 0
            ans = 0
            for c in range(_m+1):
                mm = math.comb(_m, c) * pow(nums[i], c, MOD)%MOD
                f = flag + c
                ans += mm * dp(_m-c, _k-(f%2), i+1, f//2)
            return ans % MOD
        return dp(m, k, 0, 0)
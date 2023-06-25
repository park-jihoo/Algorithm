class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dp(i, fuel):
            if fuel < 0:
                return 0
            res = 1 if i == finish else 0
            for j in range(len(locations)):
                if j == i:
                    continue
                res += dp(j, fuel - abs(locations[i]-locations[j]))
                res %= 10**9 + 7
            return res
        return dp(start, fuel)
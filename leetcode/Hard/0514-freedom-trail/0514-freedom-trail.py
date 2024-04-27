class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # String DP DFS BFS
        n = len(ring)
        matches = defaultdict(list)
        dp = {}
        for idx, val in enumerate(ring):
            matches[val].append(idx)
            if val == key[0]:
                dp[idx] = 1 + min(idx, n-idx)
        for i in range(1, len(key)):
            dp2 = {}
            for c in matches[key[i]]:
                dp2[c] = float('inf')
                for idx, val in dp.items():
                    dp2[c] = min(dp2[c], 1+min(abs(c-idx), n-abs(c-idx))+val)
            dp = dp2
        return min(dp.values())
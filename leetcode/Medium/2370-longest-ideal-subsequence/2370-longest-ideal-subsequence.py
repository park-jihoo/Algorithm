class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        ans = [1] * n
        charmap = defaultdict(list)

        dp = [0] * 26

        for idx, char in enumerate(s):
            curr = ord(char) - ord("a")

            for i in range(max(curr - k, 0), min(curr + k + 1, 26)):
                ans[idx] = max(ans[idx], dp[i] + 1)

            dp[curr] = max(dp[curr], ans[idx])
            charmap[curr].append(idx)

        return max(ans)

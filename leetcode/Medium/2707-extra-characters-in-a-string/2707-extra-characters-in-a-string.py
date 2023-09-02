class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        max_val = len(s) + 1
        dp = [max_val] * (len(s) + 1)
        dp[0] = 0
        dict_set = set(dictionary)

        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1] + 1

            for l in range(1, i + 1):
                if s[i - l : i] in dict_set:
                    dp[i] = min(dp[i], dp[i - l])

        return dp[-1]

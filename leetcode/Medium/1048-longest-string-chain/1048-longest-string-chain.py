class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        length = sorted(words, key=len)
        dp = {x: len(x) for x in words}
        for w in length:
            max1 = 0
            for i in range(len(w)):
                pre = w[:i] + w[i + 1 :]
                max1 = max(max1, dp.get(pre, 0) + 1)
                dp[w] = max1
                print(max1)
        return max(dp.values())

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        cnt1 = s.count("1")

        n = len(s)
        i = 0

        bestGain = 0
        prev = -inf

        while i < n:
            start = i

            while i < n and s[i] == s[start]:
                i += 1

            if s[start] == "0":
                cur = i - start
                bestGain = max(bestGain, prev + cur)
                prev = cur

        return cnt1 + bestGain
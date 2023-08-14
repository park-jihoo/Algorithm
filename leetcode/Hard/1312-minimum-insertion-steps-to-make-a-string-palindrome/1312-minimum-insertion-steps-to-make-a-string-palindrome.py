class Solution:
    @cache
    def minInsertionUtil(self, s, start, end):
        if start > end:
            return len(s)
        elif start == end:
            return 0
        elif start == end - 1:
            return 0 if s[start] == s[end] else 1
        elif s[start] == s[end]:
            return self.minInsertionUtil(s, start + 1, end - 1)
        else:
            return (
                min(
                    self.minInsertionUtil(s, start + 1, end),
                    self.minInsertionUtil(s, start, end - 1),
                )
                + 1
            )

    def minInsertions(self, s: str) -> int:
        # OMG Hard Again
        # String, DP
        return self.minInsertionUtil(s, 0, len(s) - 1)

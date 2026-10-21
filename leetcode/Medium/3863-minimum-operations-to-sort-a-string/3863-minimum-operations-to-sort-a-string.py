class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        mn = mx = s[0]
        isSorted = 1

        for i in range(1, n):
            if s[i] < s[i - 1]:
                isSorted = 0
            mn = min(mn, s[i])
            mx = max(mx, s[i])

        if isSorted: return 0
        if n == 2: return -1
        if s[0] == mn or s[-1] == mx:
            return 1

        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        return 3
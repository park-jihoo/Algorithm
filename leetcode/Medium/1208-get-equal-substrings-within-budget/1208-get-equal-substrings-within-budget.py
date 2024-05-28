class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        maxlen, start, curr = 0, 0, 0
        for i in range(len(s)):
            curr += costs[i]
            while curr > maxCost:
                curr -= costs[start]
                start += 1
            maxlen = max(maxlen, i - start + 1)

        return maxlen
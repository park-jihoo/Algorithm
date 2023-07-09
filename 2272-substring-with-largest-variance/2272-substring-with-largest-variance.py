class Solution:
    def kadane(self, a: str, b: str, s: str) -> int:
        ans = 0
        countA = 0
        countB = 0
        canExtendPrevB = False

        for c in s:
            if c != a and c != b:
                continue
            if c == a:
                countA += 1
            else:
                countB += 1
            if countB > 0:
                ans = max(ans, countA - countB)
            elif countB == 0 and canExtendPrevB:
                ans = max(ans, countA - 1)

            if countB > countA:
                countA = 0
                countB = 0
                canExtendPrevB = True
        return ans

    def largestVariance(self, s: str) -> int:
        return max(self.kadane(c1, c2, s)
            for c1 in string.ascii_lowercase
            for c2 in string.ascii_lowercase
            if c1 != c2)

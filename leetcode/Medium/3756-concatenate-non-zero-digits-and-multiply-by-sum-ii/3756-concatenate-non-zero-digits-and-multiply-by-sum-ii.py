class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n, ans, mod = len(s), [], 10**9 + 7
        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * 10) % mod
        a, b, L = [[0] * (n + 1) for _ in range(3)]
        for i in range(n):
            d = int(s[i])
            a[i + 1] = a[i] + d
            b[i + 1] = (b[i] * 10 + d) % mod if d else b[i]
            L[i + 1] = L[i] + (d > 0)

        for l, r in queries:
            r += 1

            sub = (b[l] * power[L[r] - L[l]]) % mod
            x = (b[r] - sub) % mod
            ans.append((x * (a[r] - a[l])) % mod)

        return ans

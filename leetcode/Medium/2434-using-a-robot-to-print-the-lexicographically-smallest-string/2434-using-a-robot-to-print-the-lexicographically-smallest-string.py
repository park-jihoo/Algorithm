class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        p, t = [], []
        suf = [""] * n
        suf[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(s[i], suf[i + 1])
        for i in range(n):
            t.append(s[i])
            while t and (i == n - 1 or t[-1] <= suf[i + 1]):
                p.append(t.pop())
        return "".join(p)

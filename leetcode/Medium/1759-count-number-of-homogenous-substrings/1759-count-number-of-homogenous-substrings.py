class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        mod = 10 ** 9 + 7
        for k, g in groupby(s):
            x = len(list(g))
            ans += (x * (x+1))//2
            ans %= mod
        return ans % mod

    def countHomogenous2(self, s: str) -> int:
        strs = []
        mod = 10 ** 9 + 7
        for a in s:
            if len(strs) == 0:
                strs.append(a)
            elif strs[-1][0] == a:
                strs[-1] += a
            else:
                strs.append(a)
        lenstr = [(len(x)*(len(x) + 1)//2)%mod for x in strs]
        return sum(lenstr)%mod
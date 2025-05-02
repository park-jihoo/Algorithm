class Solution:
    def cmp(self, a, b):
        return int(a > b) - int(a < b)
    def pushDominoes(self, dominoes: str) -> str:
        s = [(i, x) for i, x in enumerate(dominoes) if x != "."]
        s = [(-1, 'L')] + s + [(len(dominoes), 'R')]
        ans = list(dominoes)
        for (i, x), (j, y) in zip(s, s[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y:
                for k in range(i+1, j):
                    ans[k] = '.LR'[self.cmp(k-i, j-k)]
        return "".join(ans)
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans, cur = [], []
        def dfs(o, c):
            if o == 0 and c == 0:
                ans.append(''.join(cur))
                return
            if o > 0:
                cur.append('(')
                dfs(o-1, c)
                cur.pop()
            if c > o:
                cur.append(')')
                dfs(o, c-1)
                cur.pop()
        dfs(n, n)
        return ans
class Solution:
    def processStr(self, s: str) -> str:
        ans = ""
        for c in s:
            if c == '#':
                ans += ans
            elif c == '%':
                ans = ans[::-1]
            elif c == "*":
                if len(ans) != 0:
                    ans = ans[:-1]
            else:
                ans += c
        return "".join(ans)
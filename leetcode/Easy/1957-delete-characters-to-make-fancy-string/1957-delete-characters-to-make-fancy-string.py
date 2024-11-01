class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            if i == 0:
                pass
            elif i == len(s) - 1:
                pass
            elif s[i - 1] == s[i] and s[i] == s[i + 1]:
                continue
            ans.append(s[i])
        return "".join(ans)

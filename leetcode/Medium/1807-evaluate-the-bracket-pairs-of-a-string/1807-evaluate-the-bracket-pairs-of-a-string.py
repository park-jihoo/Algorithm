class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        stack = ""
        ans = ""
        flag = True
        km = {x[0]: x[1] for x in knowledge}
        for i in range(len(s)):
            if s[i] == "(":
                flag = False
            elif s[i] == ")":
                ans += km.get(stack, "?")
                stack = ""
                flag = True
            elif flag:
                ans += s[i]
            else:
                stack += s[i]
        return ans
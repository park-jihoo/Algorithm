class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ""
        for c in s:
            if c == "(":
                if len(stack) > 0:
                    ans += "("
                stack.append(")")
            if c == ")":
                stack.pop()
                if len(stack) > 0:
                    ans += ")"
        return ans

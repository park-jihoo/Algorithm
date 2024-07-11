class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque()
        ans = []
        for let in s:
            if let == "(":
                stack.append(len(ans))
            elif let == ")":
                start = stack.pop()
                ans[start:] = ans[start:][::-1]
            else:
                ans.append(let)
        return "".join(ans)

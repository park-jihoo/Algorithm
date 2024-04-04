class Solution:
    def maxDepth(self, s: str) -> int:
        stack = deque()
        ans = 0
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")":
                ans = max(ans, len(stack))
                stack.pop()
            else:
                ans = max(ans, len(stack))
        return ans

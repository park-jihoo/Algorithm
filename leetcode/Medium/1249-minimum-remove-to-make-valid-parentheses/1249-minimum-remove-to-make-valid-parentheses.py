class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = deque()
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")" and stack:
                stack.pop()
            elif char == ")":
                s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)
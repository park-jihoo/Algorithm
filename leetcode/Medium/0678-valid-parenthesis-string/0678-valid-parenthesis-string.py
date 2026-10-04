class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = deque()
        star = []
        for idx, c in enumerate(list(s)):
            if c == "(":
                stack.append(idx)
            elif c == ")":
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(idx)
        while star and stack:
            if stack[-1] > star[-1]:
                return False
            stack.pop()
            star.pop()
        return len(stack) == 0

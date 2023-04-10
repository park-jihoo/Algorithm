from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        for c in list(s):
            if c in ['(', '{','[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if left == '(' and c == ')':
                    continue
                elif left == '[' and c == ']':
                    continue
                elif left == '{' and c == '}':
                    continue
                else:
                    return False
        return len(stack) == 0
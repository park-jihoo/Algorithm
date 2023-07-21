from collections import deque


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_idx, pop_idx, n = 0, 0, len(pushed)
        stack = deque([])
        stack.append(pushed[push_idx])
        push_idx += 1

        while stack:
            while stack[-1] != popped[pop_idx]:
                if push_idx == n:
                    return False
                stack.append(pushed[push_idx])
                push_idx += 1
            stack.pop()
            pop_idx += 1
            if len(stack) == 0 and push_idx < n:
                stack.append(pushed[push_idx])
                push_idx += 1

        return True

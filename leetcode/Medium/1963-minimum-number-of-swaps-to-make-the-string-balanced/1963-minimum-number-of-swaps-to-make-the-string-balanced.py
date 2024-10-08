class Solution:
    def minSwaps(self, s: str) -> int:
        stack = deque([])
        for idx, bracket in enumerate(s):
            if bracket == '[':
                stack.append(idx)
            elif stack:
                stack.pop()
        return (len(stack)+1)//2
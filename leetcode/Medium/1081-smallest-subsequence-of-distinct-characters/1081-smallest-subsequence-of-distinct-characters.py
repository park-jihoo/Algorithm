class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []
        for l in s:
            counter[l] -= 1
            if l in seen:
                continue
            while stack and l < stack[-1] and counter[stack[-1]]>0:
                seen.remove(stack.pop())
            stack.append(l)
            seen.add(l)
        return ''.join(stack)
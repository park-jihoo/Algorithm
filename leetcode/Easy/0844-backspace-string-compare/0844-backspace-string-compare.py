class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack = []
        tstack = []
        for i in s:
            if i == '#' and len(sstack) > 0:
                sstack.pop()
            elif i != '#':
                sstack.append(i)
        for i in t:
            if i == '#' and len(tstack) > 0:
                tstack.pop()
            elif i != '#':
                tstack.append(i)
        return sstack == tstack
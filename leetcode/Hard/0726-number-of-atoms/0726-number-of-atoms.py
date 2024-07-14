class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        elm, cnt, popped = "", 0, None
        for ch in formula + "#":
            if ch.isupper() or ch in "()#":
                if elm:
                    stack[-1][elm] += cnt if cnt else 1
                    elm = ""
                elif cnt or popped:
                    for elem, c in (popped or stack.pop()).items():
                        stack[-1][elem] += c * max(cnt, 1)
                    popped = None
                cnt = 0
            if ch == "(":
                stack.append(defaultdict(int))
            elif ch == ")":
                popped = stack.pop()
            elif ch.isdigit():
                cnt = cnt * 10 + int(ch)
            else:
                elm += ch
        return "".join(
            [f"{k}{c}" if c > 1 else k for k, c in sorted(stack.pop().items())]
        )

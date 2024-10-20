class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for e in expression:
            if e == ")":
                v = stack.pop()
                args = set()
                while v == "t" or v == "f":
                    args.add(v)
                    v = stack.pop()
                if v == "!":
                    stack.append("f" if "t" in args else "t")
                elif v == "&":
                    stack.append("f" if "f" in args else "t")
                elif v == "|":
                    stack.append("t" if "t" in args else "f")
            elif e != "(" and e != ",":
                stack.append(e)
        return stack[0] == "t"

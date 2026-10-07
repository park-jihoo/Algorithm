class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = []
        stack = [(s, 0, 0, ("(", ")"))]

        while stack:
            cur, li, lj, par = stack.pop()
            n = len(cur)
            bal = 0
            match = False

            for i in range(li, n):
                bal += (cur[i] == par[0]) - (cur[i] == par[1])
                if bal >= 0:
                    continue

                for j in range(lj, i + 1):
                    if cur[j] == par[1] and (j == lj or cur[j - 1] != par[1]):
                        nxt = cur[:j] + cur[j + 1 :]
                        stack.append((nxt, i, j, par))

                match = True
                break

            if not match:
                rev = cur[::-1]

                if par[0] == "(":
                    stack.append((rev, 0, 0, (")", "(")))
                else:
                    res.append(rev)

        return res

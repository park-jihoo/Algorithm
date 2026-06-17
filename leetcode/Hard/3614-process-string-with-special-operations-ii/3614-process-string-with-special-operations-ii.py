class Solution:
    def processStr(self, s: str, k: int) -> str:
        lens = []

        cur = 0
        for c in s:
            if c == "#":
                cur *= 2
            elif c == "%":
                pass
            elif c == "*":
                if cur:
                    cur -= 1
            else:
                cur += 1

            lens.append(cur)

        if k >= cur:
            return "."

        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            cur = lens[i]

            if c == "#":
                k %= cur // 2

            elif c == "%":
                k = cur - 1 - k

            elif c == "*":
                k = k

            else:
                if k == cur - 1:
                    return c

            if i:
                cur = lens[i - 1]
            else:
                cur = 0

        return "."

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0

        def backtrack(i, chars):
            nonlocal count
            if i == n:
                count += 1
                return "".join(chars) if count == k else ""
            for c in "abc":
                if chars and chars[-1] == c:
                    continue
                res = backtrack(i + 1, chars + [c])
                if res:
                    return res
            return ""

        return backtrack(0, [])

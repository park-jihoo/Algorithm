class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        s = "".join(list(map(str, colors)))
        n = len(s)
        s += s[: k - 1]
        red = "01" * (k // 2) + "0" * (k % 2)
        blue = "10" * (k // 2) + "1" * (k % 2)
        ans = 0
        for i in range(n):
            if s[i : i + k] in [red, blue]:
                ans += 1
        return ans

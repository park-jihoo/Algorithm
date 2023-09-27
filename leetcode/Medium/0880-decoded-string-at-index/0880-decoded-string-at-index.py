class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length, n = [0], len(s)
        for l in s:
            if l.isdigit():
                length.append(length[-1] * int(l))
            else:
                length.append(length[-1] + 1)
        for i in range(n, 0, -1):
            k %= length[i]
            if k == 0 and s[i - 1].isalpha():
                return s[i - 1]

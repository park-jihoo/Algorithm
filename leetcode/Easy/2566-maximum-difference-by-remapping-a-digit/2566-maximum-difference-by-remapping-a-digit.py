class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        n, non9, non0 = len(s), -1, -1
        for i in range(n):
            if s[i] != "9":
                non9 = i
                break
        for i in range(n):
            if s[i] != "0":
                non0 = i
                break
        ma, mi = s.replace(s[non9], "9"), s.replace(s[non0], "0")
        return int(ma) - int(mi)
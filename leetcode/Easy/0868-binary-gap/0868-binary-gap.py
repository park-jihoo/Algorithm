class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)[2:]
        s = []
        for i in range(len(n)):
            if n[i] == '1':
                s.append(i)
        m = 0
        for i in range(len(s)-1):
            j = s[(i+1)]-s[i]
            if m<j:
                m = j
        return m
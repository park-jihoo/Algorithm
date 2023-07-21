class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        c = bin(c)[2:]
        a = bin(a)[2:]
        b = bin(b)[2:]
        answer = 0
        maxlen = max(len(a), len(b), len(c))
        if len(a) < maxlen:
            a = "0" * (maxlen - len(a)) + a
        if len(b) < maxlen:
            b = "0" * (maxlen - len(b)) + b
        if len(c) < maxlen:
            c = "0" * (maxlen - len(c)) + c
        for i, j, k in zip(a, b, c):
            print(i, j, k)
            if i == "0" and j == "0" and k == "1":
                answer += 1
            elif k == "0" and int(i) + int(j) > 0:
                answer += int(i) + int(j)
        return answer

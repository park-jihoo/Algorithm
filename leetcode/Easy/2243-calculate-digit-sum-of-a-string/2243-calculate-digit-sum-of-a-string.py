class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = []  # The array representing the string after each round
            n = len(s)
            for i in range(0, n, k):
                val = 0
                for j in range(i, min(i + k, n)):
                    val += int(s[j])
                tmp.append(str(val))
            s = "".join(tmp)
        return s
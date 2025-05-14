class Solution:
    def matmul(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        n, p, q = len(a), len(b), len(b[0])
        res = [[0] * q for _ in range(n)]
        for i in range(n):
            for k in range(p):
                if a[i][k]:
                    for j in range(q):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % self.mod
        return res

    def matpow(self, mat: List[List[int]], power: int) -> List[List[int]]:
        m = 26
        res = [[int(i == j) for j in range(m)] for i in range(m)]
        while power:
            if power % 2:
                res = self.matmul(res, mat)
            mat = self.matmul(mat, mat)
            power //= 2
        return res

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        self.mod = 10 ** 9  + 7
        m = 26
        cntr = Counter(s)
        cnt = [cntr[chr(c + ord("a"))] for c in range(m)]
        mat = [[0] * m for _ in range(m)]
        for i, x in enumerate(nums):
            for j in range(x):
                mat[i][(i+j+1)%m] = 1
        cnt = [cnt]
        factor = self.matpow(mat, t)
        result = self.matmul(cnt, factor)[0]
        return sum(result)%self.mod
        
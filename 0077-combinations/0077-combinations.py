class Solution:
    def dfs(self, idx, lst):
        if len(lst) == self.k:
            self.answer.append(lst[:])
            return
        for i in range(idx, self.n):
            self.dfs(i + 1, lst + [i + 1])

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.answer = []
        self.n = n
        self.k = k
        self.dfs(0, [])
        return self.answer
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        n = len(mat)
        for i in range(n):
            ans.append([mat[i].count(1), i])

        ans.sort()
        return [i[1] for i in ans[:k]]

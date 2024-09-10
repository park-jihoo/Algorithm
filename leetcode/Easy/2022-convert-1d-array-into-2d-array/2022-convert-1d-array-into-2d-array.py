class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if len(original) != m * n:
            return []
        for idx in range(m):
            ans.append(original[idx * n : (idx + 1) * n])
        return ans

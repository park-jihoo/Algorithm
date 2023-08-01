class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(idx, lst):
            if len(lst) == k:
                answer.append(lst[:])
                return
            for i in range(idx, n):
                dfs(i + 1, lst + [i + 1])

        answer = []
        dfs(0, [])
        return answer
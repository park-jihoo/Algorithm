class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        l = list(range(1,n+1))
        def dfs(idx, lst):
            if len(lst) == k:
                answer.append(lst[:])
                return
            for i in range(idx, n):
                dfs(i+1, lst+[l[i]])
        dfs(0, [])
        return answer
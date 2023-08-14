from collections import deque, defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        graph = defaultdict(list)
        for idx, val in enumerate(arr):
            graph[val].append(idx)
        q = deque([(0, 0)])
        visited = set([0])
        while q:
            idx, step = q.popleft()
            if idx == len(arr) - 1:
                break
            neighbors = set(graph[arr[idx]] + [idx - 1, idx + 1])
            graph[arr[idx]] = []
            for n in neighbors:
                if n not in visited and 0 <= n < len(arr):
                    visited.add(n)
                    q.append((n, step + 1))
        return step

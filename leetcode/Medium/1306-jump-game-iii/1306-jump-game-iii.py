class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited, q = set([start]), deque([start])
        while q:
            node = q.popleft()
            if arr[node] == 0:
                return True
            plus, minus = node + arr[node], node - arr[node]
            if 0 <= plus < len(arr) and plus not in visited:
                q.append(plus)
                visited.add(plus)
            if 0 <= minus < len(arr) and minus not in visited:
                q.append(minus)
                visited.add(minus)
        return False

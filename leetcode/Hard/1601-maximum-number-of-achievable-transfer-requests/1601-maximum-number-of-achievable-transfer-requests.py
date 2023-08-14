class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        for k in range(len(requests), 0, -1):
            for c in itertools.combinations(range(len(requests)), k):
                degree = [0] * n
                for i in c:
                    degree[requests[i][0]] -= 1
                    degree[requests[i][1]] += 1
                if not any(degree):
                    return k
        return 0

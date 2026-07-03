class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        deg = [0] * n
        l, r = float("inf"), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            deg[v] += 1
            l = min(l, w)
            r = max(r, w)

        # Delete unreachable nodes
        q = deque([i for i in range(1, n) if deg[i] == 0])
        while q:
            u = q.popleft()
            for v, _ in g[u]:
                deg[v] -= 1
                if v and deg[v] == 0:
                    q.append(v)

        def check(mid: int) -> bool:
            dp = [math.inf] * n
            cdeg = deg.copy()
            dp[0] = 0

            q = deque([0])
            while q:
                u = q.popleft()
                if u == n - 1:
                    return dp[u] <= k

                for v, w in g[u]:
                    if w >= mid:
                        dp[v] = min(dp[v], dp[u] + w)
                    cdeg[v] -= 1
                    if cdeg[v] == 0:
                        q.append(v)
            return False

        if not check(l):
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r
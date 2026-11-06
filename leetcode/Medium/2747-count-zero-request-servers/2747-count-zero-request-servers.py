class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        server, time = zip(*sorted(logs, key=itemgetter(1)), [0, inf])  # split the logs
        cnt = [0] * (n + 1)  # requests per server inside the window [q - x, q]
        busy = lo = hi = 0  # servers with at least one request in it
        ans = [0] * len(queries)
        for i, q in sorted(enumerate(queries), key=itemgetter(1)):
            while time[hi] <= q:  # requests up to q come in
                busy += not cnt[server[hi]]
                cnt[server[hi]] += 1
                hi += 1
            while time[lo] < q - x:  # requests before q - x go out
                cnt[server[lo]] -= 1
                busy -= not cnt[server[lo]]
                lo += 1
            ans[i] = n - busy
        return ans
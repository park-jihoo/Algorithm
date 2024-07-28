class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        m = defaultdict(list)
        heap = [(0, 1)]
        d = [[] for _ in range(n + 1)]
        d[1] = [0]
        for u, v in edges:
            m[u].append(v)
            m[v].append(u)
        # second minimum time to go from 1 to n
        # green to red, red to green every changem inutes
        # enter at any time but leave only when the signal is green

        while heap:
            mind, idx = heapq.heappop(heap)
            if idx == n and len(d[n]) == 2:
                return max(d[n])
            for nbr in m[idx]:
                if (mind // change) % 2 == 0:
                    can = mind + time
                else:
                    can = math.ceil(mind / (2 * change)) * (2 * change) + time
                if not d[nbr] or (len(d[nbr]) == 1 and d[nbr] != [can]):
                    d[nbr] += [can]
                    heapq.heappush(heap, (can, nbr))
        return 0

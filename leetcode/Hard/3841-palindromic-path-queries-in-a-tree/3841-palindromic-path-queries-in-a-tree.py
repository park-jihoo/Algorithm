class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in g[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order[1:]):
            p = parent[u]
            size[p] += size[u]
            if heavy[p] == -1 or size[u] > size[heavy[p]]:
                heavy[p] = u

        head = [0] * n
        pos = [0] * n
        cur = 0

        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = cur
                cur += 1

                for v in g[u]:
                    if v != parent[u] and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        size2 = 1
        while size2 < n:
            size2 <<= 1

        seg = [0] * (2 * size2)

        for u in range(n):
            seg[size2 + pos[u]] = 1 << (ord(s[u]) - 97)

        for i in range(size2 - 1, 0, -1):
            seg[i] = seg[i * 2] ^ seg[i * 2 + 1]

        def update(p, value):
            p += size2
            seg[p] = value
            p >>= 1

            while p:
                seg[p] = seg[p * 2] ^ seg[p * 2 + 1]
                p >>= 1

        def range_query(l, r):
            l += size2
            r += size2
            res = 0

            while l <= r:
                if l & 1:
                    res ^= seg[l]
                    l += 1

                if not (r & 1):
                    res ^= seg[r]
                    r -= 1

                l >>= 1
                r >>= 1

            return res

        def path_query(u, v):
            res = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                res ^= range_query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            res ^= range_query(pos[u], pos[v])

            return res

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                update(pos[u], 1 << (ord(c) - 97))
            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_query(u, v)
                ans.append((mask & (mask - 1)) == 0)

        return ans
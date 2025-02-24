class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        g = {}
        for u, v in edges:
            if u not in g:
                g[u] = [v]
            else:
                g[u].append(v)
            if v not in g:
                g[v] = [u]
            else:
                g[v].append(u)

        parent = [0] * len(amount)
        stack = [0]

        while stack:
            u = stack.pop()
            for v in g[u]:
                stack.append(v)
                g[v].remove(u)
                parent[v] = u

        path = [bob]
        while parent[bob] != bob:
            path.append(parent[bob])
            bob = parent[bob]

        d = len(path)
        for i in range(d // 2):
            amount[path[i]] = 0
        if d % 2:
            amount[path[d // 2]] >>= 1

        stack.append(0)
        ans = -float("inf")
        while stack:
            u = stack.pop()
            if g[u]:
                for v in g[u]:
                    stack.append(v)
                    amount[v] += amount[u]
            elif ans < amount[u]:
                ans = amount[u]
        return ans

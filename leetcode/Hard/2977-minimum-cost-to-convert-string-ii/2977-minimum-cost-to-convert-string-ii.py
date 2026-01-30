class TrieNode:
    def __init__(self):
        self.children = {}
        self.to = {}


class Solution:
    def build_trie(self, min_cost):
        root = TrieNode()
        for (s, t), c in min_cost.items():
            node = root
            for ch in s:
                node = node.children.setdefault(ch, TrieNode())
            node.to[t] = min(node.to.get(t, float("inf")), c)
        return root

    def build_min_cost(self, original, changed, cost):
        by_len = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            by_len[len(o)].append((o, c, w))

        min_cost = dict()
        for L, rules in by_len.items():
            graph = defaultdict(list)
            nodes = set()

            for o, c, w in rules:
                graph[o].append((c, w))
                nodes.add(o)
                nodes.add(c)

            for s in nodes:
                dist = {s: 0}
                pq = [(0, s)]

                while pq:
                    d, u = heapq.heappop(pq)
                    if d > dist[u]:
                        continue
                    for v, w in graph[u]:
                        nd = d + w
                        if nd < dist.get(v, inf):
                            dist[v] = nd
                            heapq.heappush(pq, (nd, v))

                for t, d in dist.items():
                    min_cost[(s, t)] = min(min_cost.get((s, t), inf), d)

        return min_cost

    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        n = len(source)
        min_cost = self.build_min_cost(original, changed, cost)
        trie = self.build_trie(min_cost)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == inf:
                continue

            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            node = trie
            for j in range(i, n):
                ch = source[j]
                if ch not in node.children:
                    break
                node = node.children[ch]

                t_sub = target[i : j + 1]
                if t_sub in node.to:
                    dp[j + 1] = min(dp[j + 1], dp[i] + node.to[t_sub])

        return -1 if dp[n] == inf else dp[n]

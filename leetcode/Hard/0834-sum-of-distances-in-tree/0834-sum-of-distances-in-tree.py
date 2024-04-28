class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        sums = [0] * n
        counts = [0] * n

        def dfs(node, parent):
            count = 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    count += dfs(neighbor, node)
                    sums[node] += sums[neighbor] + counts[neighbor]
            counts[node] = count
            return count

        dfs(0, -1)

        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    sums[neighbor] = sums[node] - counts[neighbor] + (n - counts[neighbor])
                    dfs2(neighbor, node)

        dfs2(0, -1)

        return sums
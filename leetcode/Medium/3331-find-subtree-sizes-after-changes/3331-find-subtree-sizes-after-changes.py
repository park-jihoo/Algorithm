class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        graph = defaultdict(list)
        for i in range(1, len(parent)):
            graph[parent[i]].append(i)

        n = len(parent)
        ans = [1] * n

        def dfs(node, letters):
            c = s[node]
            letters[c].append(node)

            for child in graph[node]:
                x = dfs(child, letters)
                ans[node] += x

            letters[c].pop()

            if letters[c]:
                ans[letters[c][-1]] += ans[node]
                return 0
            else:
                return ans[node]

        dfs(0, defaultdict(list))
        return ans
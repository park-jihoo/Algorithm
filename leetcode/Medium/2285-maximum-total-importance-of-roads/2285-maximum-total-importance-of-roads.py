class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        road = Counter()
        ans = 0
        for s, e in roads:
            road[s] += 1
            road[e] += 1
        for idx, (key, val) in enumerate(road.most_common()):
            ans += (n - idx) * val
        return ans
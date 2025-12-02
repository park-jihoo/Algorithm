class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        hm, mod = defaultdict(int), 10**9+7
        for x, y in points:
            hm[y] += 1
        hm = [(x*(x-1)//2)%(mod) for x in hm.values()]
        return ((sum(hm) * sum(hm) - sum(x*x for x in hm))//2)%mod
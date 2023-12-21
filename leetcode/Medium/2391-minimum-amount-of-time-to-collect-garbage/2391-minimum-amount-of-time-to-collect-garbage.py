class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = sum(len(g) for g in garbage)
        G, P, M = False, False, False
        for i in range(len(travel), 0, -1):
            G |= 'G' in garbage[i]
            P |= 'P' in garbage[i]
            M |= 'M' in garbage[i]
            ans += travel[i-1] * (G + P + M)
        
        return ans
        
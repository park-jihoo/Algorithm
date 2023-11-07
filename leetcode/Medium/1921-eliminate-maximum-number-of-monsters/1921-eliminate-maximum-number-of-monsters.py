class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = sorted([d/s for d, s in zip(dist, speed)])
        ans = 0
        for idx, arr in enumerate(arrival):
            if arr <= idx:
                break
            ans += 1
        return ans
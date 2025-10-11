class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ks = [[] for _ in range(k)]
        for idx, val in enumerate(energy):
            ks[idx % k].append(val)
        ans = float("-inf")
        for kl in ks:
            ans = max(ans, *accumulate(reversed(kl)))
        return ans

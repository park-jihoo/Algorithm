class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        numu = []
        for i in nums:
            if numu and numu[-1] == i:
                continue
            numu.append(i)
        for i in range(1, len(numu) - 1):
            if (numu[i - 1] - numu[i]) * (numu[i + 1] - numu[i]) > 0:
                ans += 1
        return ans

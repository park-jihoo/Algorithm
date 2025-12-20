class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in range(len(strs[0])):
            sc = [x[i] for x in strs]
            ans += sorted(sc) != sc
        return ans

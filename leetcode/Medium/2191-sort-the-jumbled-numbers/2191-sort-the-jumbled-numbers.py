class Solution:
    def mapint(self, num):
        ans = ""
        for x in list(str(num)):
            ans += self.mapdict[x]
        return int(ans)

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        self.mapdict = {str(idx): str(val) for idx, val in enumerate(mapping)}
        return sorted(nums, key=lambda x: self.mapint(x))

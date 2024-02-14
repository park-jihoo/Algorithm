class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        ans = []
        for x, y in zip(pos, neg):
            ans.extend([x, y])
        return ans
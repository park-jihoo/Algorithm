class Solution:
    def transform(self, num):
        if num == 1:
            return 1
        else:
            return -1

    def findMaxLength(self, nums: List[int]) -> int:
        h = defaultdict(list)
        s = 0
        ans = 0
        for idx in range(len(nums)):
            s += self.transform(nums[idx])
            h[s].append(idx)
        for key, li in h.items():
            if key == 0:
                ans = max(ans, li[-1] + 1)
            elif len(li) > 1:
                ans = max(ans, li[-1] - li[0])
        return ans

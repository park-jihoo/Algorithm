class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = {0:1}
        cnt, ans = 0, 0
        for idx, num in enumerate(nums):
            cnt += (num % 2)
            if cnt - k in d:
                ans += d[cnt - k]
            d[cnt] = d.get(cnt, 0) + 1
        return ans
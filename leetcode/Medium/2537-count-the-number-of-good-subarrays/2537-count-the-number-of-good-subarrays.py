class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        fr = defaultdict(int)
        ans, cnt, left = 0, 0, 0
        for r, x in enumerate(nums):
            cnt += fr[x]
            fr[x] += 1
            while cnt >= k:
                ans += n - r
                fr[nums[left]] -= 1
                cnt -= fr[nums[left]]
                left += 1
        return ans

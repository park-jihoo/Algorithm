class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n, d = len(nums), len(set(nums))
        cnt = defaultdict(int)
        left, ans = 0, 0
        for right in range(len(nums)):
            cnt[nums[right]] += 1
            while len(cnt) == d:
                ans += (n - right)
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
        return ans
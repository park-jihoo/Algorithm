class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt, ans, left, right = defaultdict(int), 0, 0, 0
        for num in nums:
            cnt[num] += 1
            if cnt[num] == 1:
                k -= 1
                if k < 0:
                    cnt[nums[right]] = 0
                    right += 1
                    left = right
            if k <= 0:
                while cnt[nums[right]] > 1:
                    cnt[nums[right]] -= 1
                    right += 1
                ans += right - left + 1
        return ans

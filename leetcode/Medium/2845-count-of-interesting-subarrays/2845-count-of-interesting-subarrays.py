class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n, ans, pref = len(nums), 0, 0
        cnt = Counter([0])
        for i in range(n):
            pref += int(nums[i] % modulo == k)
            ans += cnt[(pref-k+modulo)%modulo]
            cnt[pref%modulo]+=1
        return ans
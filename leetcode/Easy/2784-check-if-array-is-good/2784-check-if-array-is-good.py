class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n+1:
            return False
        cnt = Counter(nums)
        if len(cnt) != n:
            return False
        if cnt[n] != 2:
            return False
        return True
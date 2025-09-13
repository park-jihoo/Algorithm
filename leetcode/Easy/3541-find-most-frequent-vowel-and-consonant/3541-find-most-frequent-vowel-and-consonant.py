class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = Counter(s)
        return max(cnt[x] for x in 'aeiou') + max(cnt[x] for x in 'bcdfghjklmnpqrstvwxyz')
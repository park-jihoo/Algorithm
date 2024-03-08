class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = 0
        m = Counter(nums).most_common()[0][1]
        for idx, cnt in Counter(nums).most_common():
            if cnt == m:
                ans += m
        return ans
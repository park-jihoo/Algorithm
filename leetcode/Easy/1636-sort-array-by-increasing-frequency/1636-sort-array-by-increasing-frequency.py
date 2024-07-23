class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(sorted(nums))
        ans = []
        for val, cnt in cnt.most_common():
            ans = [val] * cnt + ans
        return ans

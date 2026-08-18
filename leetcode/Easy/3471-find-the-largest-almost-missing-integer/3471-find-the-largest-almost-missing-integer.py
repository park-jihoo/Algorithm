class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        cnt, n = Counter(), len(nums)
        for i in range(n - k + 1):
            cnt += Counter(set(nums[i : i + k]))
        ans = max((num for num, val in cnt.most_common() if val == 1), default=-1)
        return ans

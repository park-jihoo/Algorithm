class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            cnt = Counter(nums[i : i + k])
            freq = sorted(cnt.items(), key=lambda v: (-v[1], -v[0]))
            xsum = sum(k * v for k, v in freq[:x])
            ans.append(xsum)
        return ans

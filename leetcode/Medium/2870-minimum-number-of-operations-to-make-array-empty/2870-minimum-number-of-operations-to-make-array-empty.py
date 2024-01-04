class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for val, cnt in Counter(nums).most_common():
            if cnt == 1:
                return -1
            else:
                ans += (cnt - 1) // 3 + 1
        return ans

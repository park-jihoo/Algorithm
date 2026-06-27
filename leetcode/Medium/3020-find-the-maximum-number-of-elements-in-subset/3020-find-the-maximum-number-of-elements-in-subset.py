class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        one = cnt.get(1, 0)

        ans = one if one % 2 else one - 1
        cnt.pop(1, None)

        for num in cnt:
            tmp, x = 0, num
            while x in cnt and cnt[x] > 1:
                tmp += 2
                x *= x
            ans = max(ans, tmp + (1 if x in cnt else -1))
        return ans

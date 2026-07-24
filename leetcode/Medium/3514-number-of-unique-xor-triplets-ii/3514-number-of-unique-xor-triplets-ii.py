class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX = 2048

        pair = [False] * MAX
        for a in nums:
            for b in nums:
                pair[a ^ b] = True

        ans = [False] * MAX
        for x in range(MAX):
            if pair[x]:
                for a in nums:
                    ans[x ^ a] = True

        return sum(ans)
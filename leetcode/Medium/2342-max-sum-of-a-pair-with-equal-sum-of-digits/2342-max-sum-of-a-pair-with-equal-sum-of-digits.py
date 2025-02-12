class Solution:
    def sumDigits(self, n):
        d = str(n)
        return sum(int(s) * d.count(s) for s in "123456789")

    def maximumSum(self, nums: List[int]) -> int:
        mp = {}
        ans = -1
        for num in nums:
            dgt = self.sumDigits(num)
            print(num, dgt, ans)
            if dgt in mp:
                ans = max(ans, mp[dgt] + num)
                mp[dgt] = max(mp[dgt], num)
            else:
                mp[dgt] = num
        return ans
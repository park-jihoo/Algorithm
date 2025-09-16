class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        curr = nums[0]
        for x in nums[1:]:
            if gcd(curr, x) > 1:
                curr = lcm(curr, x)
                while ans and gcd(curr, ans[-1]) > 1:
                    curr = lcm(curr, ans.pop())
            else:
                ans.append(curr)
                curr = x
        ans.append(curr)
        return ans
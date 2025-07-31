class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = {0}
        for x in arr:
            cur = {x|y for y in cur} | {x}
            ans |= cur
        return len(ans)
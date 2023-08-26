class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])
        curr = float("-inf")
        ans = 0
        for pair in pairs:
            if pair[0] > curr:
                ans += 1
                curr = pair[1]
        return ans

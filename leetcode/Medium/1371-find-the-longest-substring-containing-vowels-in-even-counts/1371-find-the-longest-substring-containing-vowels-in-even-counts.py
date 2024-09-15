class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # a, e, i, o, u in even times
        cm = [0] * 26
        cm[0] = 1
        cm[ord("e") - ord("a")] = 2
        cm[ord("i") - ord("a")] = 4
        cm[ord("o") - ord("a")] = 8
        cm[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        ans = 0
        prefix = 0
        for i, c in enumerate(s):
            prefix ^= cm[ord(c) - ord("a")]
            if mp[prefix] == -1 and prefix != 0:
                mp[prefix] = i
            ans = max(ans, i - mp[prefix])
        return ans

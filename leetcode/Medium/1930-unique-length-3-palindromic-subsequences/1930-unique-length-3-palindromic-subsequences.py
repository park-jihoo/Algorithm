class Solution:
    def countPalindromicSubsequence(self, s):
        ans = 0
        for c in string.ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                ans += len(set(s[i + 1 : j]))
        return ans

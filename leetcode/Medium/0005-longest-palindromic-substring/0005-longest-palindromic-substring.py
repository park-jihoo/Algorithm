class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [0, 0]
        table = [[False]*n for _ in range(n)]
        for i in range(n): # string length equals to 1
            table[i][i] = True
        for i in range(n-1): # string length equals to 2
            if s[i] == s[i+1]:
                table[i][i+1] = True
                ans = [i, i+1]
        for l in range(2, n+1): # string length more than 3
            for i in range(n - l):
                j = l+i
                if s[i] == s[j] and table[i+1][j-1]:
                    table[i][j] = True
                    ans = [i, j]
        
        return s[ans[0]:ans[1]+1]
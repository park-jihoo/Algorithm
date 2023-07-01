class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.ans = float('inf')
        self.cookies = cookies
        self.k = k

        self.dfs(0, [0]*k)
        
        return self.ans

    def dfs(self, s, children):
        max_cookies = max(children)
        if max_cookies >= self.ans:
            return

        if s == len(self.cookies):
            self.ans = min(self.ans, max_cookies)
            return

        for i in range(self.k):
            children[i] += self.cookies[s]
            self.dfs(s + 1, children)
            children[i] -= self.cookies[s]
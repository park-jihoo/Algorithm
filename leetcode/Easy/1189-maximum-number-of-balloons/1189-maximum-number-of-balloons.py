class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt, bal, ans = Counter(text), Counter("balloon"), 0
        while cnt >= bal:
            cnt -= Counter("balloon")
            ans += 1
        return ans

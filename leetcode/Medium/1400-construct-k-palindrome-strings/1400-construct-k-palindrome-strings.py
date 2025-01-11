class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = Counter(s)
        odd = len([key for key, val in cnt.items() if val%2==1])
        return k >= odd and k <= len(s)
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = [s[i:i+k] for i in range(0, len(s), k)]
        if len(ans[-1]) < k:
            ans[-1] += fill * (k - len(ans[-1]))
        return ans
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0 for x in code]
        d = code + code
        if k > 0:
            return [sum(d[idx + 1 : idx + k + 1]) for idx in range(n)]
        else:
            return [sum(d[idx + n + k : idx + n]) for idx in range(n)]

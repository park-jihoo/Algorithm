class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for a, b in queries:
            tmp, lst = 0, a
            for i in range((a.bit_length()+1)//2, (b.bit_length()+1)//2+1):
                tmp += i * (min(b+1, 4**i) - lst)
                lst = min(b+1, 4 ** i)
            ans += (tmp + 1) // 2
        return ans
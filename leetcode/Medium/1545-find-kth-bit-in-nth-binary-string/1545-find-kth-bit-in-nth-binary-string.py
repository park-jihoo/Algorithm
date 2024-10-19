class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # s_n -> (2^n - 1) 2->2, 3->4, 4->8
        if k == 1:
            return "0"
        elif k == 2 ** (n - 1):
            return "1"
        elif k < 2 ** (n-1):
            return self.findKthBit(n-1, k)
        else:
            return str(1 - int(self.findKthBit(n-1, 2**n - k)))
        return ""
        
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        result = 0
        for i, val in enumerate(bin(n)[2:][::-1]):
            if val == '0':
                result += pow(2, i)
        return result
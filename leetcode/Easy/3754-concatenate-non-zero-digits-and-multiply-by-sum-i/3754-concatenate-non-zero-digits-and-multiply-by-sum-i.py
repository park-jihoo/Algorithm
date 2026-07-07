class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = str(n).replace('0', '')
        if x == '':
            x = '0'
        return int(x) * sum(map(int, x))
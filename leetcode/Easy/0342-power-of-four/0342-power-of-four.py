class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        binary = str(bin(n))[2:]
        if binary[0] != "1":
            return False
        if len(binary) % 2 != 1:
            return False
        if binary.count("0") == len(binary) - 1:
            return True
        return False

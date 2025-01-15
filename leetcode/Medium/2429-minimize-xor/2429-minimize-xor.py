class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bit_diff = num1.bit_count() - num2.bit_count()
        while bit_diff != 0:
            if bit_diff > 0:
                bit_diff -= 1
                num1 &= num1 - 1
            else:
                bit_diff += 1
                num1 |= num1 + 1
        return num1

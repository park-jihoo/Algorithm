class Solution:
    def totalMoney(self, n: int) -> int:
        div, mod = divmod(n, 7)
        return (mod * (mod + 1)) // 2 + 28 * div + mod * div + 7 * div * (div - 1) // 2

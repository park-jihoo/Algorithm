class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        on, en = n // 2 + n % 2, n // 2
        om, em = m // 2 + m % 2, m // 2
        return on*em + en*om
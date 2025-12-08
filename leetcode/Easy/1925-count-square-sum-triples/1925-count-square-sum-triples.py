class Solution:
    def countTriples(self, n: int) -> int:
        squares = [x**2 for x in range(1, n + 1)]
        ans = 0
        for a, b in product(squares, squares):
            if a != b and (a + b) in squares:
                ans += 1
        return ans

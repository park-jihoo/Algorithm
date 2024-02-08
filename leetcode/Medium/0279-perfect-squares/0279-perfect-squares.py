class Solution:
    def numSquares(self, n):
        if n < 2:
            return n
        squares = [i * i for i in range(1, int(n**0.5) + 1)]

        count = 0
        to_check = {n}
        while to_check:
            count += 1
            next_to_check = set()

            for x in to_check:
                for square in squares:
                    if x == square:
                        return count

                    if x < square:
                        break

                    next_to_check.add(x - square)

            to_check = next_to_check

        return count

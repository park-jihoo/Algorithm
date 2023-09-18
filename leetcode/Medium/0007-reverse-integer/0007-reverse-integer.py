class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        r= 0
        while x != 0:
            if r > MAX_INT/10 or r<MIN_INT/10:
                return 0
            digit = x % 10 if x > 0 else x % -10
            r = r * 10 + digit
            x = math.trunc(x/10)
        return r
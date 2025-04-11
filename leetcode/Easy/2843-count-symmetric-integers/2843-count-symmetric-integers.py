class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            if math.ceil(math.log10(i)) == 2 and i % 11 == 0:
                ans += 1
            elif math.ceil(math.log10(i)) == 4:
                left, right = divmod(i, 100)
                if left % 10 + left // 10 == right % 10 + right // 10:
                    ans += 1
        return ans

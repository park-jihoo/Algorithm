class Solution:
    def factor(self, num):
        factors = Counter({})
        if num < 0:
            return self.factor(-1 * num) + Counter({-1: 1})
        if num == 0:
            return Counter({0: 1})

        i = 2

        while i <= num:
            if num % i == 0:
                factors[i] += 1
                num = num / i
            else:
                i += 1
        return factors

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = sum([self.factor(num) for num in nums], start=Counter())
        exc = [p - self.factor(num) for num in nums]
        return [prod(x**y for x, y in c.items()) for c in exc]

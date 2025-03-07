class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = set(range(left, right + 1))
        primes -= set([1])
        for i in range(2, math.ceil(math.sqrt(right)) + 1):
            primes -= set(range(i * 2, right + 1, i))
        if len(primes) < 2:
            return [-1, -1]
        primes = sorted(list(primes))
        ans = [primes[0], primes[1]]
        for i in range(1, len(primes) - 1):
            if primes[i + 1] - primes[i] < ans[1] - ans[0]:
                ans = [primes[i], primes[i + 1]]
        return ans

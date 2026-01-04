class Solution:
    def find_primes(self, n):
        che = [False, False] + [True] * (n - 1)
        primes = []
        for i in range(2, n + 1):
            if che[i]:
                primes.append(i)
                for j in range(i * 2, n + 1, i):
                    che[j] = False
        return primes

    def sumFourDivisors(self, nums: List[int]) -> int:
        primes = self.find_primes(max(nums))
        ans = 0
        for num in nums:
            for p in primes:
                if num // p != p and num / p in primes:
                    ans += num // p + p + 1 + num
                    break
                if num == p**3:
                    ans += 1 + p + p**2 + p**3
                    break
        return ans

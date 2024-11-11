class Solution:
    def find_primes(self, n):
        che = [False, False] + [True] * (n - 1)
        primes = []
        for i in range(2, n + 1):
            if che[i]:
                primes.append(i)
                for j in range(i * 2, n + 1, i):
                    che[j] = False
        return [0] + primes

    def minmaxprime(self, primes, n):
        start, end = 0, len(primes) - 1
        while start <= end:
            mid = (start + end) // 2
            if primes[mid] < n:
                start = mid + 1
            else:
                end = mid - 1
        return primes[start - 1]

    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = self.find_primes(max(nums))
        nums[0] -= self.minmaxprime(primes, nums[0])
        for idx in range(1, len(nums)):
            if nums[idx] <= nums[idx - 1]:
                return False
            else:
                nums[idx] -= self.minmaxprime(primes, nums[idx] - nums[idx - 1])
        return True

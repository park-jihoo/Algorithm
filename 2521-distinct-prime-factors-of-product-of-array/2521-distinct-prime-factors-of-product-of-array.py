class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def getFactor(n):
            n_sqrt = int(n**1 / 2) + 1
            factorset = set()
            for i in range(2, n_sqrt):
                while n % i == 0:
                    factorset.add(i)
                    n /= i
            if len(factorset) == 0:
                factorset.add(n)
            return factorset

        answerset = set()
        for i in nums:
            answerset.update(getFactor(i))
        return len(answerset)

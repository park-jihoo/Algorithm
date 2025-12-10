class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        val = complexity[0]
        for i in range(1, len(complexity)):
            if complexity[i] <= val:
                return 0
        return math.factorial(len(complexity) - 1) % (10**9+7)
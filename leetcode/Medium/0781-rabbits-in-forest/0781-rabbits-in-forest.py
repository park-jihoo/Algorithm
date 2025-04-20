class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum(math.ceil(v/(x+1))*(x+1) for x, v in Counter(answers).items())
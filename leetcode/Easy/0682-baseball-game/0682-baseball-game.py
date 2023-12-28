class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for i in ops:
            if i == "+":
                score.append(score[-1] + score[-2])
            elif i == "D":
                score.append(score[-1]*2)
            elif i == "C":
                score.pop()
            else:
                score.append(int(i))
        return sum(score)
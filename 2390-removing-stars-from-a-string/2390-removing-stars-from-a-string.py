
class Solution:
    def removeStars(self, s: str) -> str:
        answer = []
        for c in s:
            if c == '*' and len(answer) > 0:
                answer.pop()
            else:
                answer.append(c)
        return ''.join(answer)
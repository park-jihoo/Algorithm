class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answer = 0
        maxcount = 0
        table = defaultdict(int)
        start = 0
        for idx, a in enumerate(answerKey):
            table[a == "T"] += 1
            maxcount = max(maxcount, table[a == "T"])
            while maxcount + k < idx - start + 1:
                table[answerKey[start] == "T"] -= 1
                start += 1
            answer = max(answer, idx - start + 1)
        return answer

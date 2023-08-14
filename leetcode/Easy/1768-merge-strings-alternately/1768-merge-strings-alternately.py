class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        for i in range(min(len(word1), len(word2))):
            answer.append(word1[i])
            answer.append(word2[i])
        if len(word1) > len(word2):
            answer.append(word1[len(word2) :])
        elif len(word1) < len(word2):
            answer.append(word2[len(word1) :])
        return "".join(answer)

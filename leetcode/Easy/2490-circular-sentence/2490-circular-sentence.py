class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        senlst = sentence.split()
        if senlst[0][0] != senlst[-1][-1]:
            return False
        for i in range(len(senlst) - 1):
            if senlst[i][-1] != senlst[i + 1][0]:
                return False
        return True

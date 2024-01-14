class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cnt1, cnt2 = Counter(word1), Counter(word2)
        if cnt1.keys() != cnt2.keys():
            return False
        for (char1, idx1), (char2, idx2) in zip(cnt1.most_common(), cnt2.most_common()):
            if idx1 != idx2:
                return False
        return True

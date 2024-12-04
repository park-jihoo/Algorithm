class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx2 = 0
        len1, len2 = len(str1), len(str2)

        for idx1 in range(len1):
            if idx2 < len2 and (ord(str2[idx2]) - ord(str1[idx1]))%26 <= 1:
                idx2 += 1
        return idx2 == len2
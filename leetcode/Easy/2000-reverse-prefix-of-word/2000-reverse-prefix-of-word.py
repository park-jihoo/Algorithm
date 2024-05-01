class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            idx = word.index(ch)
            return word[idx::-1] + word[idx+1:]
        except:
            return word
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        slist = sentence.split()
        for idx, word in enumerate(slist):
            if word.startswith(searchWord):
                return idx+1
        return -1
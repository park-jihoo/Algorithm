class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x:len(x))
        ans = []
        for i, word in enumerate(words):
            for j in range(i+1, len(words)):
                if word in words[j]:
                    ans.append(word)
                    break
        return ans
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans, cur = [], ""
        for word in words:
            if Counter(cur) == Counter(word):
                continue
            cur = word
            ans.append(cur)
        return ans
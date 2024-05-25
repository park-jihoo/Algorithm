class Solution:
    def wordList(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        ans = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                ans.append(word)
            else:
                rst = self.wordList(s[len(word) :], wordDict, memo)
                for item in rst:
                    item = word + " " + item
                    ans.append(item)
        memo[s] = ans
        return ans

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        slist = self.wordList(s, wordDict, {})
        return slist

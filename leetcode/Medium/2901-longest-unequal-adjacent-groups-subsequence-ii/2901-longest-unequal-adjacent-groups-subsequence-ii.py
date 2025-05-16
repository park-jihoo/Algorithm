class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if len(words) == 1: return words

        @cache
        def dist(w1, w2):
            d = 0
            i = 0
            while i < len(w1) and i < len(w2):
                if w1[i] != w2[i]:
                    d += 1
                i += 1
            if i < len(w1): 
                d += len(w1) - len(w2)
            elif i < len(w2): 
                d += len(w2) - len(w1)
            return d
        
        adj = defaultdict(list)
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) == len(words[j]) and dist(words[i], words[j]) <= 1 and groups[i] != groups[j]:
                    adj[words[i]].append(words[j])
        
        @cache
        def dfs(word):
            if word not in adj: 
                return [word]
            res = []
            for w in adj[word]:
                r = dfs(w)
                if len(r) > len(res):
                    res = r
            return [word] + res
        
        res = []
        for w in words:
            r = dfs(w)
            if len(r) > len(res):
                res = r
        return res
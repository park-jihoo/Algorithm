class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = deque(sorted([x for x in list(s) if x.lower() in list('aeiou')]))
        idx = 0
        ans = []
        for i in range(len(s)):
            if s[i].lower() not in list('aeiou'):
                ans.append(s[i])
            else:
                ans.append(vowels[0])
                vowels.popleft()
        return "".join(ans)
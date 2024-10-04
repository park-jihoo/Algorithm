class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = sum(skill) // (len(skill)//2)
        cnt_skl = Counter(skill)
        ans = 0
        if s % 2 == 0:
            if cnt_skl[s//2] % 2 == 0:
                ans += (cnt_skl[s//2]//2) * (s//2) * (s//2)
            else:
                return -1
        for i in range((s+1) // 2):
            if cnt_skl[i] != cnt_skl[s-i]:
                return -1
            else:
                ans += cnt_skl[i] * i * (s-i)
        return ans
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        ans = 0
        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            ans += count[key]
            count[key] += 1
        return ans

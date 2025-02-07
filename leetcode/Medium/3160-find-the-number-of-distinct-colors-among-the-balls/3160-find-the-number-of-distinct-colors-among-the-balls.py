class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans, colors, cnt, uniq = [], {}, Counter(), 0
        for ball, color in queries:
            if ball in colors:
                prev = colors[ball]
                cnt[prev] -= 1
                if cnt[prev] == 0:
                    uniq -= 1
            colors[ball] = color
            if cnt[color] == 0:
                uniq += 1
            cnt[color] += 1
            
            ans.append(uniq)
        return ans
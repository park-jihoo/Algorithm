class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = Counter(x[0] for x in matches)
        loser = Counter(x[1] for x in matches)
        players = set(winner | loser )
        return [sorted(list(players - set(loser))),sorted([x for x, cnt in loser.items() if cnt == 1])]
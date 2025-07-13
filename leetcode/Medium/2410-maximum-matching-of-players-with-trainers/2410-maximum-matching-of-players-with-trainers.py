class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort(reverse=True)
        players.sort(reverse=True)
        ans, pi = 0, 0
        for ti in range(len(trainers)):
            while pi < len(players):
                if players[pi] <= trainers[ti]:
                    pi += 1
                    ans += 1
                    break
                else:
                    pi += 1
        return ans

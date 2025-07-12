class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        firstPlayer -= 1
        secondPlayer -= 1

        @lru_cache(None)
        def dfs(mask: int, round_num: int) -> (int, int):
            players = [i for i in range(n) if (mask & (1 << i))]
            m = len(players)

            for i in range(m // 2):
                a, b = players[i], players[-1 - i]
                if (a == firstPlayer and b == secondPlayer) or (
                    a == secondPlayer and b == firstPlayer
                ):
                    return (round_num, round_num)

            next_masks = []

            def dfs_match(idx, curr_mask):
                if idx >= (m + 1) // 2:
                    next_masks.append(curr_mask)
                    return
                a, b = players[idx], players[-1 - idx]
                if a == firstPlayer or a == secondPlayer:
                    dfs_match(idx + 1, curr_mask | (1 << a))
                elif b == firstPlayer or b == secondPlayer:
                    dfs_match(idx + 1, curr_mask | (1 << b))
                else:
                    dfs_match(idx + 1, curr_mask | (1 << a))
                    dfs_match(idx + 1, curr_mask | (1 << b))

            curr_mask = 0
            if m % 2 == 1:
                middle = players[m // 2]
                curr_mask |= 1 << middle
            dfs_match(0, curr_mask)

            earliest, latest = float("inf"), 0
            for nm in next_masks:
                e, l = dfs(nm, round_num + 1)
                earliest = min(earliest, e)
                latest = max(latest, l)
            return (earliest, latest)

        init_mask = (1 << n) - 1
        return list(dfs(init_mask, 1))

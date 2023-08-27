class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)
        memo = {}

        def dfs(position, jump):
            if position == stones[-1]:
                return True

            if (position, jump) in memo:
                return memo[(position, jump)]

            for next_jump in range(max(jump - 1, 1), jump + 2):
                next_position = position + next_jump
                if next_position in stones_set:
                    if dfs(next_position, next_jump):
                        memo[(position, jump)] = True
                        return True

            memo[(position, jump)] = False
            return False

        return dfs(0, 0)
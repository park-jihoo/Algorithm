class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for idx, val in enumerate(rating):
            llc, rgc, lgc, rlc = 0, 0, 0, 0
            for left in rating[:idx]:
                if left < val:
                    llc += 1
                if left > val:
                    lgc += 1
            for right in rating[idx + 1 :]:
                if right > val:
                    rgc += 1
                if right < val:
                    rlc += 1
            ans += llc * rgc + lgc * rlc
        return ans

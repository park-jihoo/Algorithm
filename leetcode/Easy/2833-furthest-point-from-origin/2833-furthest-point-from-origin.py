class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt = Counter(moves)
        return max(
            abs(cnt["L"] - cnt["R"] - cnt["_"]), abs(cnt["L"] - cnt["R"] + cnt["_"])
        )

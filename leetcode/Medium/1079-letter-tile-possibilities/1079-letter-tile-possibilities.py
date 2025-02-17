class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnts = Counter(tiles)
        def back():
            ans = 0
            for key, val in cnts.items():
                if val:
                    cnts[key] -= 1
                    ans += 1 + back()
                    cnts[key] += 1
            return ans
        return back()
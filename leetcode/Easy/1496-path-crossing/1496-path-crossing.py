from collections import Counter


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pathlist = list(path)
        visited = [(0, 0)]
        x, y = 0, 0
        for p in pathlist:
            if p == "N":
                x += 1
            elif p == "E":
                y += 1
            elif p == "W":
                y -= 1
            else:
                x -= 1
            visited.append((x, y))

        c2 = Counter(visited)
        return c2.most_common()[0][1] != 1

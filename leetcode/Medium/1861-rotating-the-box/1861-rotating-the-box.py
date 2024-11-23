class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rotatedBox = []
        for row in box:
            stone, empty, ans = 0, 0, []
            for cell in row:
                if cell == "#":
                    stone += 1
                elif cell == "*":
                    ans += empty * ["."] + stone * ["#"] + ["*"]
                    stone, empty = 0, 0
                else:
                    empty += 1
            ans += empty * ["."] + stone * ["#"]
            rotatedBox.append(ans)

        m, n = len(box), len(box[0])
        return [[rotatedBox[m - j - 1][i] for j in range(m)] for i in range(n)]

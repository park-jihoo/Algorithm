import sys
from itertools import permutations

N = int(sys.stdin.readline())
game = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = float("-inf")
order = [i for i in range(1, 9)]
for x in permutations(order, 8):
    x = list(x)
    batter = x[:3] + [0] + x[3:]
    number, score = 0, 0
    for i in range(N):
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out < 3:
            if game[i][batter[number]] == 0:
                out += 1
            elif game[i][batter[number]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif game[i][batter[number]] == 2:
                score += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif game[i][batter[number]] == 3:
                score += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            else:
                score += base1 + base2 + base3 + 1
                base1, base2, base3 = 0, 0, 0
            number = (number + 1) % 9
    ans = max(ans, score)
print(ans)

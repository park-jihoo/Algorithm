class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d, cur_x, cur_y = 0, 0, 0
        obstacles = set([(x, y) for x,y in obstacles])
        ans = 0
        for c in commands:
            if c == -2:
                cur_d = (cur_d-1)%4
            elif c == -1:
                cur_d = (cur_d+1)%4
            else:
                for i in range(c):
                    dx, dy = cur_x + d[cur_d][0], cur_y + d[cur_d][1]
                    if (dx, dy) in obstacles:
                        break
                    cur_x, cur_y = dx, dy
            ans = max(ans, cur_x*cur_x + cur_y*cur_y)
        return ans
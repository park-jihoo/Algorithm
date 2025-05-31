class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        newboard = [0]
        for i in range(n - 1, -1, -2):
            newboard.extend(board[i])
            if i - 1 >= 0:
                newboard.extend(board[i - 1][::-1])
        q = [1]
        vis = set()
        steps = 0
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if node == n * n:
                    return steps
                if node in vis:
                    continue
                vis.add(node)
                for neig in range(1, 7):
                    next_node = node + neig
                    if next_node <= n * n:
                        dest = newboard[next_node] if newboard[next_node] != -1 else next_node
                        if dest not in vis:
                            q.append(dest)
            steps += 1
        return -1
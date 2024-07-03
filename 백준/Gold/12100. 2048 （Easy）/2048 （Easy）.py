# acmicpc 12100 2048 (Easy)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def rotate90(board):
    new_board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[j][n - 1 - i] = board[i][j]
    return new_board


def convert(lst):
    new_lst = [i for i in lst if i]
    for i in range(len(new_lst) - 1):
        if new_lst[i] == new_lst[i + 1]:
            new_lst[i] *= 2
            new_lst[i + 1] = 0
    new_lst = [i for i in new_lst if i]
    return new_lst + [0] * (len(lst) - len(new_lst))


def dfs(n, board, count):
    ret = max([max(i) for i in board])
    if count == 0:
        return ret
    for _ in range(4):
        x = [convert(i) for i in board]
        if x != board:
            ret = max(ret, dfs(n, x, count - 1))
        board = rotate90(board)
    return ret


print(dfs(n, board, 5))

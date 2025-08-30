class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            tmp = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in tmp:
                    return False
                tmp.add(board[i][j])
        for i in range(9):
            tmp = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in tmp:
                    return False
                tmp.add(board[j][i])
        for i in range(3):
            for j in range(3):
                tmp = set()
                for a in range(3):
                    for b in range(3):
                        if board[3 * i + a][3 * j + b] == ".":
                            continue
                        elif board[3 * i + a][3 * j + b] in tmp:
                            return False
                        tmp.add(board[3 * i + a][3 * j + b])
        return True

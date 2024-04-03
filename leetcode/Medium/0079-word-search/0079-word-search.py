class Solution:
    def dfs(self, board, i, j, word):

        adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if len(word) == 0:
            return True
        if not (
            0 <= i < len(board) and 0 <= j < len(board[0]) and word[0] == board[i][j]
        ):
            return False
        tmp = board[i][j]
        board[i][j] = "#"
        res = (
            self.dfs(board, i + 1, j, word[1:])
            or self.dfs(board, i - 1, j, word[1:])
            or self.dfs(board, i, j + 1, word[1:])
            or self.dfs(board, i, j - 1, word[1:])
        )
        board[i][j] = tmp
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs(board, i, j, word):
                    return True
        return False

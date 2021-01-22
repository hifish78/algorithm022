class Solution:
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.dfs(click[0], click[1], board)
        return board

    def dfs(self, x, y, board):
        m, n = len(board), len(board[0])
        if x < 0 or x >= m or y < 0 or y >= n:
            return
        if board[x][y] != 'E':
            return

        cnt = self.search_around(x, y, board)
        if cnt != 0:
            board[x][y] = str(cnt)  ## Do NOT forget convert to str , use "str(cnt)" instead of "cnt"
            return ## DO NOT miss this line!!!!

        board[x][y] = 'B'

        for i, j in self.dirs:
            self.dfs(x + i, y + j, board)

    def search_around(self, x, y, board):
        cnt = 0
        for i, j in self.dirs:
            new_x = x + i
            new_y = y + j
            if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):
                continue
            if board[new_x][new_y] == 'M':
                cnt += 1
        return cnt



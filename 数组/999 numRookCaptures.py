class Solution:
    def numRookCaptures(self, board):
        r = 0
        c = 0
        for r in range(8):
            for c in range(8):
                if board[r][c] == "R":
                    break
            if board[r][c] == "R":
                break

        self.r = r
        self.c = c
        self.board = board

        output = self.up() + self.left() + self.down() + self.right()
        #output = self.up()
        return output

    def up(self):
        get = 0
        for _r in range(self.r, -1, -1):
            if self.board[_r][self.c] == 'p':
                get += 1
                return get
            if self.board[_r][self.c] == 'B':
                return get
        return get

    def left(self):
        get = 0
        for _c in range(self.c, -1, -1):
            if self.board[self.r][_c] == 'p':
                get += 1
                return get
            if self.board[self.r][_c] == 'B':
                return get
        return get

    def down(self):
        get = 0
        for _r in range(self.r,8):
            if self.board[_r][self.c] == 'p':
                get += 1
                return get
            if self.board[_r][self.c] == 'B':
                return get
        return get

    def right(self):
        get = 0
        for _c in range(self.c,8):
            if self.board[self.r][_c] == 'p':
                get += 1
                return get
            if self.board[self.r][_c] == 'B':
                return get
        return get

sol = Solution()
input =[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

print(sol.numRookCaptures(input))
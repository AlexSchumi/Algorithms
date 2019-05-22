class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        """
        First implementation of solving sudoku using brutal force, check every row and column and every small cube;
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        if not board or len(board) == 0:
            return False

        a2 = list(zip(*board))
        # check every row and column in board
        for i in range(9):
            #row = map(lambda v: self.checkDuplicates(v[0]), board)
            #col = map(lambda v: self.checkDuplicates(v[1]), board)
            row = self.checkDuplicates(board[i])
            col = self.checkDuplicates(a2[i])
            if row == False or col == False:
                return False
        # check every submatrix in board
        loc = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]

        for l in loc:
            if not self.checkDuplicates2(l[0], l[1], board):
                return False
        return True

    def checkDuplicates(self, vector):
        d = []
        for n in vector:
            if n != ".":
                if n in d:
                    return False
                else:
                    d.append(n)
                if int(n) < 1 or int(n) > 9:
                    return False
        return True

    def checkDuplicates2(self, x, y, board):
        d = []
        for i in range(3):
            for j in range(3):
                if board[x+i][y+j] != ".":
                    if board[x+i][y+j] in d:
                        return False
                    else:
                        d.append(board[x+i][y+j])
                    if int(board[x+i][y+j]) < 1 or int(board[x+i][y+j]) > 9:
                        return False
        return True

    """
    This is difficult implementation of valid sudoku using some trick for searching for small cube;
    Time complexity: O(n^2)
    Space complexity: O(n)
    """

    def isValidSudoku2(self, board):
        if not board or len(board) == 0:
            return False

        for i in range(len(board)):
            row = []
            col = []
            cube = []
            for j in range(len(board[0])):
                # check small cube
                row_idx = (i // 3) * 3# 0 0 0 3 3 3 6 6 6
                col_idx = (i % 3) * 3 # 0 3 6 0 3 6 0 3 6
                if board[i][j] != '.':
                    if board[i][j] in row: # check row
                        return False
                    else:
                        row.append(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in col: # check col
                        return False
                    else:
                        col.append(board[j][i])
                if board[row_idx + j % 3][col_idx + j //3] != '.':
                    if board[row_idx + j % 3][col_idx + j //3] in cube:
                        return False
                    else:
                        cube.append(board[row_idx + j % 3][col_idx + j //3])
        return True

board = [[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]
print(Solution().isValidSudoku2(board))

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        """
        This is my implementation for sudoku solver
        Time complexity:
        Space complexity:
        """
        if not board or len(board) == 0:
            return board
        self.solve(board)
        print(board)

    def solve(self, board):
        candidate = [str(k) for k in range(1,10)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.': # we have to fill out this cell
                    for number in candidate: # candidate number to fill in
                        if self.isValid(board, i, j, number):
                            board[i][j] = number
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, i, j, c):
        for idx in range(9):
            if board[i][idx] != "." and board[i][idx] == c:
                return False
            if board[idx][j] != "." and board[idx][j] == c:
                return False
            if board[3*(i//3)+idx%3][3*(j//3)+idx//3] != "." and board[3*(i//3)+idx%3][3*(j//3)+idx//3]==c:
                    return False
        return True


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],\
[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],\
["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],\
[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],\
[".",".",".",".","8",".",".","7","9"]]


Solution().solveSudoku(board)

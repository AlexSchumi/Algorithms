class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        """
        My first implementation of word search : TLE
        Time complexity:
        Space complexity: O(n)
        """
        if not board or len(board) == 0:
            return False

        if not word:
            return False

        #used = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    #res = self.dfs(word, "", board, i, j, used, loc) # get dfs in this board location
                    if self.dfs3(i, j, board, word, 0):
                        return True
        return False

    def dfs(self, word, res, board, i, j, used, loc):
        m = len(board)
        n = len(board[0])
        if res == word:
            return True
        if i < 0 or j < 0 or i >= m or j >= n or len(res) > len(word):
            return False

        if [i,j] not in used:
            if board[i][j] != word[loc]:
                return False
            return self.dfs(word, res+board[i][j], board, i+1, j, used+[[i,j]], loc+1)\
            or self.dfs(word, res+board[i][j], board, i-1, j, used+[[i,j]], loc+1)\
            or self.dfs(word, res+board[i][j], board, i, j+1, used+[[i,j]], loc+1)\
            or self.dfs(word, res+board[i][j], board, i, j-1, used+[[i,j]], loc+1)

    def dfs2(self, word, board, i, j, loc):
        m = len(board)
        n = len(board[0])
        if loc >= len(word):
            return True

        if i < 0 or j < 0 or i >= m or j >= n or word[loc] != board[i][j]:
            return False

        tmp = board[i][j]
        board[i][j] = '#' # change board word to make it as used 1.use used to mark used grid 2.write it as # to mark
        res = self.dfs2(word, board, i+1, j, loc+1)\
        or self.dfs2(word, board, i-1, j, loc+1)\
        or self.dfs2(word, board, i, j+1, loc+1)\
        or self.dfs2(word, board, i, j-1, loc+1)
        board[i][j] = tmp
        return res

    def dfs3(self,i, j, board, word, loc):
        m = len(board)
        n = len(board[0])

        if loc >= len(word):
            return True

        if i < 0 or i >= m or j < 0 or j >= n or word[loc] != board[i][j]:
            return False

        tmp = board[i][j]
        board[i][j] = '*' # marked grid
        res =  self.dfs3(i+1, j, board, word, loc+1) or self.dfs3(i-1, j, board, word, loc+1)\
        or self.dfs3(i, j+1, board, word, loc+1) or self.dfs3(i, j-1, board, word, loc+1)
        board[i][j] = tmp
        return res



board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = "ABCCED"
print(Solution().exist(board, word))

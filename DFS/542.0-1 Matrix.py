import sys
import copy
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[None] * len(matrix[0]) for i in range(len(matrix))]
        if not matrix:
            return res

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited = [[0] * len(matrix[0]) for i in range(len(matrix))] # create a visited matrix for backtracking
                if matrix[i][j] == 0:
                    res[i][j] = 0 # dist from 0 -> 0 is 0
                else:
                    res[i][j] = self.dfs(i, j, res, matrix, visited)
        return res

    """
    !!!!!!!!!!!!!!!!!!!!!! Remember always backtracking in graph traversal to avoid stackoverflow!!!!!!!!!!!!!!!!!!!!!!!!!
    """


    """
    A dfs helper function to search around the 0 around the (i,j)!!!! review it again//
    """
    def dfs(self, i, j, res, matrix, visited):
        m = len(matrix)
        n = len(matrix[0])

        if (i < 0 or i >= m or j < 0 or j >= n): # if we have reached the boundary of matrix
            return sys.maxsize - 1

        if matrix[i][j] == 0:
            return 0

        if visited[i][j] == 0:
            visited[i][j] = 1 # backtrack in this case to remember the visited node
            return min(self.dfs(i+1, j, res, matrix, visited) + 1, self.dfs(i-1, j, res, matrix, visited) + 1,\
            self.dfs(i, j+1, res, matrix, visited) + 1, self.dfs(i, j-1, res, matrix, visited) + 1)

    """
    I used bfs to implement this quesion for shortest path, but it will TLE?????? FXXK
    """
    def updateMatrix2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0] * len(matrix[0]) for i in range(len(matrix))] # all of res are 0 with initialization;
        if not matrix or len(matrix) == 0:
            return res
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0: # if this is 1, we have to find nearest 0;
                    queue = []
                    visited = [[0] * n for k in range(m)] # create a visited matrix for backtracking
                    level = 0
                    visited[i][j] = 1 # mark this node
                    if (0 <= i - 1 < m):
                        queue.append((i-1,j))
                    if (0 <= i + 1 < m):
                        queue.append((i+1,j))
                    if (0 <= j + 1 < n):
                        queue.append((i,j+1))
                    if (0 <= j - 1 < n):
                        queue.append((i,j-1))

                    while queue and res[i][j] == 0:
                        size = len(queue)
                        level += 1
                        for adj in range(size):
                            row, col = queue.pop(0) # pop from the left
                            visited[row][col] = 1
                            if matrix[row][col] == 0:
                                res[i][j] = level
                                break
                            else: # append the next level adj nodes in queue
                                if (0 <= row - 1 < m) and visited[row-1][col] == 0: # always append valid index into queue
                                    queue.append((row-1,col))
                                if (0 <= row + 1 < m) and visited[row+1][col] == 0:
                                    queue.append((row+1,col))
                                if (0 <= col + 1 < n) and visited[row][col+1] == 0:
                                    queue.append((row, col+1))
                                if 0 <= col-1 < n and visited[row][col-1] == 0:
                                    queue.append((row, col-1))
        return res

    """
    This is implementation of bfs by starting from 0 instead of 1 in the previous one
    Time complexity: O(mn)
    Space complexity: O(mn)
    """
    def updateMatrix3(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        res = copy.deepcopy(matrix)
        queue = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i,j))
                else:
                    res[i][j] = sys.maxsize - 1

        d1 = [1,0,-1,0]
        d2 = [0,1,0,-1]
        while queue:
            x, y = queue.pop(0)
            for idx in range(4):
                dx = x + d1[idx]
                dy = y + d2[idx]
                if dx >= 0 and dy >= 0 and dx < m and dy < n and res[dx][dy] > res[x][y] + 1:
                    res[dx][dy] = res[x][y] + 1
                    queue.append((dx, dy))
        return res


print(Solution().updateMatrix3([[0,0,0],[0,1,0],[1,1,1]]))

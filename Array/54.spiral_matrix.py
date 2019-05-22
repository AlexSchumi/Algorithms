"""
Time complexity: O(m x n)
Space complexity: O(m x n)
"""

def spiralOrder(matrix):
    res = []
    if not matrix or len(matrix) == 0:
        return res
    rows = 0
    rowe = len(matrix) - 1
    cols = 0
    cole = len(matrix[0]) - 1

    while rows <= rowe and cols <= cole:
        #if rows == rowe:
        #    for i in range(cols, cole + 1):
        #        res.append(matrix[rows][i])
        #    return res
        for i in range(cols, cole+1):
            res.append(matrix[rows][i])
        rows += 1

        for i in range(rows, rowe+1):
            res.append(matrix[i][cole])
        cole -= 1

        if rows <= rowe:
            for i in range(cole, cols-1, -1):
                res.append(matrix[rowe][i])
        rowe -= 1

        if cols <= cole:
            for i in range(rowe, rows-1, -1):
                res.append(matrix[i][cols])
        cols += 1

        #if rows == rowe:
        #    for i in range(cols, cole):
        #        res.append(matrix[rows][i])
    return res

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
if __name__ == "__main__":
    print(spiralOrder(matrix))

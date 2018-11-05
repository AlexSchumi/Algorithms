def spiralOrder(matrix):
    if not matrix:
        return matrix
    nrow = len(matrix)
    ncol = len(matrix[0])

    res = []
    if nrow == 1: # edge case when we have only one row or one column of matrix
        return matrix[0]
    if ncol == 1:
        return matrix[0][0]

    row_len =  ncol  # starting number of elements in row
    col_len =  nrow - 1 # starting number of elements in col

    row_start = 0
    row_end = row_len
    row_idx = 0  # which row we are in

    col_start = 1
    col_end = col_len
    col_idx = ncol - 1 # which col we are in

    while row_len > 1 and col_len > 1:
        res.append(matrix[row_idx][row_start:row_end])
        res.append(matrix[col_start:col_end][col_idx])
        row_len -= 1
        row_end = col_idx
        row_start = row_end - row_len
        row_idx = col_end
        col_len -= 1
        col_start = row_end - 1
        col_end =
        col_idx = row_end
    return res

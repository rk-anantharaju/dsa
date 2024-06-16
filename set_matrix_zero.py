'''
https://leetcode.com/problems/set-matrix-zeroes/description/

https://takeuforward.org/data-structure/set-matrix-zero/

'''

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in matrix]))
    col0 = 1
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                if col == 0:
                    col0 = 0
                else:
                    matrix[0][col] = 0    
   
    print("\n")
    print(col0)
    print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in matrix]))
    
    print("rows is ", row, "  cols is ", col)
    for row in range(1, rows):
        for col in range(1, cols):
            if matrix[row][col] !=0 and (matrix[0][col] == 0 or matrix[row][0] == 0):
                matrix[row][col] = 0

    # print("\n")
    # print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in matrix]))
    
    if matrix[0][0] == 0:
        for col in range(cols):
            matrix[0][col] = 0
    if col0 == 0:
        for row in range(rows):
            matrix[row][0] = 0    
    print("\n")
    print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in matrix]))
    





matrix = [[0,1,1],[1,0,1],[1,1,1]]


# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = [[1],[0],[3]]
# matrix = [[1,0,3]]
setZeroes( matrix)
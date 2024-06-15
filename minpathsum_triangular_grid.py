triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]

# https://takeuforward.org/data-structure/minimum-path-sum-in-triangular-grid-dp-11/
def minimum_path_sum_traingle(triangle):
    print("input data ", triangle)
    size = len(triangle)

    # create dp array
    dp_arr = [[0 for i in range(size)] for j in range(size)]
    # print(dp_arr)

    # for each row in the triangle
    for row in range(size-1, -1, -1):
        # print(row)
        # for each column in the traingle, # of cols is equal to row number. 
        # as we are taking zero index, no need to increase col count, it can be same as row value
        for col in range (row, -1, -1):
            if row == size -1:
                dp_arr[row][col] = triangle[row][col]
                continue

            diag =  dp_arr[row+1][col+1] + triangle[row][col] 
            down =    dp_arr[row+1][col] + triangle[row][col]  
            
            dp_arr[row][col] = min (diag, down)

        print ("row # ", row, "  dp arr is ",dp_arr)    
    return dp_arr[0][0]


# https://leetcode.com/problems/minimum-path-sum/description/
grid = [[1,3,1],[1,5,1],[4,2,1]]
# grid = [[1,2,3],[4,5,6]]
grid = [[1,2],[1,1]]
import sys

def minimum_path_sum_rect(grid):
    print (grid)
    # define dp arr
    rows = len(grid)
    cols = len (grid[0])

    dp_arr = [[0 for i in range(cols)] for j in range(rows)]
    # print (dp_arr)
    for row in range(rows):
        for col in range(cols):
            
            down = sys.maxsize
            right = sys.maxsize
            if col == 0 and row == 0:
                dp_arr[row][col] = grid [row][col]
                continue

            if row > 0:    
                down = grid[row][col] + dp_arr[row-1][col]

            if col > 0:
                right = grid [row][col] + dp_arr[row][col-1]    

            dp_arr[row][col] = min (down, right) #+ grid[row][col]
            
        print ("row # ", row, "  dp arr is ",dp_arr)     
    return dp_arr[-1][-1]
    pass



# print(minimum_path_sum_traingle(triangle))
print(minimum_path_sum_rect(grid))

#https://takeuforward.org/data-structure/3-d-dp-ninja-and-his-friends-dp-13/


def cherry_pickup_dp(grid):
    rows =  len(grid)
    cols =  len(grid[0])

    dp_arr =  [[[0 for x in range(cols)] for y in range(cols)] for z in range(rows)]
        
    '''
    in recursion
    # given start point is fixed and destination is vairalbe i.e last row's any cell 
    # hence we have termiantion when we reach the last row and ensure both are not on same cell, if its same cell use value once. 
    
    when recursion is converted to tabulation, change the "top down" appraoch to "botton up" so we start from last row to 0,0 cell in tabulation
    '''
    for j1 in range(cols):
        for j2 in range(cols):
            if j1 == j2:
                dp_arr[rows-1][j1][j2] = grid[rows-1][j1]
            else:    
                dp_arr[rows-1][j1][j2] = grid[rows-1][j1] + grid[rows-1][j2]


            
    # begin from last but one row and go towards 0  
    for i in range(rows -2, -1, -1 ):
        # check for each cell combination i.e bot can start from any cell in the last row
        # h3ence it doesn't mattter if we go from 0 to cols or cols to 0 in the loops
        # get the max value when start from anyn cell combo in a given row
        import sys
        
        for j1 in range(cols):
            for j2 in range(cols):
            
                maxval = -sys.maxsize
                # try all the 9 possible moves, i.e when first robot start from a cell, second one can have 3 moves
                for x1 in [-1, 0, 1]:
                    for  x2 in  [-1, 0, 1]:
                        collection = 0
                        # # have valiation for out of boundaies
                        if (j1+ x1 < 0 or j1 + x1 >= cols or j2+ x2 < 0 or j2 + x2 >= cols ):
                            continue 

                        # if both are on same cell, use value only once
                        if j1 == j2:
                            collection = grid[i][j1]
                        else:    
                            collection = grid[i][j1] + grid[i][j2]

                        # if (j1+ x1 < 0 or j1 + x1 >= cols or j2+ x2 < 0 or j2 + x2 >= cols ):
                        # # if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):    
                        #     collection = int(-1e8)
                        # else:    
                        #     collection =  collection + dp_arr[i+1][j1+x1][j2+x2]
                        collection =  collection + dp_arr[i+1][j1+x1][j2+x2]    

                        maxval = max(maxval, collection)
                # Store the maximum chocolates collected in the memoization table
                dp_arr[i][j1][j2] = maxval            
    
    return dp_arr[0][0][cols- 1]
                                   

     
grid = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
    #  = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]

print(cherry_pickup_dp(grid))



import sys

# Function to find the maximum chocolates collected
def maximumChocolates(grid):
    n = len(grid)
    m = len(grid[0])
    # Initialize a 3D memoization table dp with zeros
    dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]

    # Initialize the values for the last row of dp based on grid values
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                dp[n - 1][j1][j2] = grid[n - 1][j1]
            else:
                dp[n - 1][j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

    # Iterate through rows from the second-to-last row to the first row
    for i in range(n - 2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = -sys.maxsize

                # Try out 9 possible options by changing the indices
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]

                        if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):
                            ans += int(-1e9)  # A large negative value if out of bounds
                        else:
                            ans += dp[i + 1][j1 + di][j2 + dj]  # Add the value from the next row

                        maxi = max(ans, maxi)

                # Store the maximum chocolates collected in the memoization table
                dp[i][j1][j2] = maxi
    # Return the maximum chocolates collected in the top row and the last column
    return dp[0][0][m - 1]


print(maximumChocolates(grid))

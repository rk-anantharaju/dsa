#https://leetcode.com/problems/cherry-pickup/description/

def get_maxpath(grid):
    rows = len(grid)
    cols = len(grid[0]) 
    dp_arr = [[0 for x in range(cols)] for y in range(rows)]
    # print(dp_arr)

    for i in range (rows-1, -1, -1):
      up  = 0
      left = 0
      for j in range(cols-1, -1, -1):
        
        if i == rows-1 and j == cols-1 or grid[i][j] == -1 :
            dp_arr[i][j] = grid[i][j]
            continue

        if j < cols-1:
        #    if dp_arr[i][j-1] != -1:
            left = dp_arr[i][j+1]
        
        if i < rows-1:
        #    if dp_arr[i-1][j] != -1:
            up = dp_arr[i+1][j]

        dp_arr[i][j]  = max(up, left) + grid[i][j] if max(up, left) >=0 else -1 

        # print ("row ", i, " col ", j , " grid[i][j]",  grid[i][j], "left ", left, " up ", up )
        
        # if left > up:
        #     dp_arr[i][j-1] = 0
        # elif up > left:
        #    dp_arr[i-1][j] = 0
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXX YYYYYYYYYYYYYYYYYYYYYYYYY")
    print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in dp_arr]))
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXX retunr valueseeeeeeeeeeeee")
    
    return dp_arr
    
    

def cherry_pickup(grid):
    grid_l = grid[:]
    # print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in grid_l]))
    rows = len(grid)
    cols = len(grid[0]) 
    
    # print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in dp_arr]))
    dp_arr = get_maxpath(grid)
    forwardvalue = dp_arr[0][0]
    #  
    print("forwardvalue ", forwardvalue)

    if forwardvalue > 0:
        print("original griddddddddddd")
        print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in grid]))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
        for i in range (rows):
            for j in range(cols):
                # print (dp_arr[i][j])
                
                if j < cols-1 and dp_arr[i][j] - dp_arr[i][j+1] == 1:
                    grid_l[i][j-1] = 0
                    
                if i < rows-1 and dp_arr[i][j] - dp_arr[i+1][j] == 1:
                    grid_l[i-1][j] = 0
                    
        grid_l[-1][-1] = 0
        
        print ("grid after removing forward values")
        print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in grid_l]))
        print(grid_l)

        dp_arr2 = get_maxpath(grid_l)   

        reversevalue = dp_arr2[0][0]

        if reversevalue > 0:
            forwardvalue = forwardvalue + reversevalue       
    
        print("reversevalue ", reversevalue)
 
    print (dp_arr)                   
    return forwardvalue if forwardvalue >0 else 0







grid = [[1,1,-1],
        [1,-1,1],
        [-1,1,1]] # output = 0

grid = [[0,1,-1],
        [1,0,-1],
        [1,1,1]] # output =5
grid = [[0,1,-1],[1,0,-1],[1,1,1]]
# grid = [[1]]

grid = [
[1,1,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,1],
[1,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,1,1]]

# grid = [[0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 1], 
#         [1, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0]]
# print(cherry_pickup(grid))



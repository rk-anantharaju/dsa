import sys
# Input: n = 4, heights = [20, 30, 40, 20]
# Output: 20

heights = [20, 30, 40, 20]
heights = [10, 20, 30, 10]
heights = [30, 20, 50, 10, 40]
def find_steps1(heights):
    steps = len(heights) 
    steps_arr = [0]*steps
    # bottom to top
    for i in range(steps):
        onestep = 0
        #define max integer
        twostep = sys.maxsize

        # print(heights[i])
        if i == 0:
            steps_arr[i] = 0
            continue
            
        onestep = steps_arr [i-1] + abs(heights[i] - heights[i-1])
        
        if i > 1:
            twostep = steps_arr [i-2] + abs(heights[i] - heights[i-2])
            
        # print(onestep, twostep)    

        steps_arr[i] = min(onestep, twostep)
        # print(steps_arr)
    # print(steps_arr)    
    return steps_arr[-1]   

# top to bottom down approach
def find_steps_recursion(heights, position):
    steps = len(heights) 

    onestep = 0
        #define max integer
    twostep = sys.maxsize

    if position == 0:
        return 0
    
    if steps_arr[position] != -1:
        return steps_arr[position]
    
    onestep = find_steps_recursion(heights, position-1) + abs(heights[position] - heights[position-1])
    
    if position > 1:
       twostep = find_steps_recursion(heights, position-2) + abs(heights[position] - heights[position-2])
        
    steps_arr[position] = min(onestep, twostep)
    
    return steps_arr[position]   



print("input: ", heights)
print(find_steps1(heights))

steps_arr = [-1]*(len(heights))
# print(steps_arr)
print(find_steps_recursion(heights, len(heights)-1))
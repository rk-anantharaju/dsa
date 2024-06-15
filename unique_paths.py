'''
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3

https://leetcode.com/problems/unique-paths/description/

https://takeuforward.org/data-structure/grid-unique-paths-dp-on-grids-dp8/

'''

def unique_paths_recursion(m, n, data_array):
    """
        :type m: int
        :type n: int
        :rtype: int
    """
    if data_array[m][n] != -1:
        return data_array[m][n]

    if m < 0 or n < 0:
        return 0

    if m == 0 and n == 0:
        return 1
           
    upmove = unique_paths_recursion(m-1, n, data_array)
    leftmove = unique_paths_recursion(m, n-1, data_array)
    data_array[m][n] = upmove + leftmove
    # print(data_array)
    return data_array[m][n]

def unique_paths_tabulation(m, n):
    data_array = [[0 for i in range(n)] for j in range(m)]
    
    for row in range(m):
        for col in range(n):
           if row == 0 and col == 0:
              data_array[row][col] = 1
              continue
        #    print(row, col)
           upmove = 0
           leftmove = 0
           if row -1 > -1:
                # print("calculagtion upmove for row, col", row, col)
                upmove = data_array[row-1][col] 
           
           if col -1 > -1:
                # print("calculagtion leftmove for row, col", row, col)
                leftmove = data_array[row][col-1]    

           data_array[row][col] = upmove + leftmove
        #    print(data_array)
    return data_array[-1][-1]       

m, n = 3 , 7 
# m, n = 3 , 2

#define memoization matrix
data_array = [[-1 for i in range(n)] for j in range(m)]

print(unique_paths_recursion(m-1, n-1, data_array))      
print(unique_paths_tabulation(m,n))
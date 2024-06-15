grid = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]

# Define the first function
def cherry_pickup_dp(grid):
    rows = len(grid)
    cols = len(grid[0])

    dp_arr = [[[0 for x in range(cols)] for y in range(cols)] for z in range(rows)]

    for j1 in range(cols):
        for j2 in range(cols):
            if j1 == j2:
                dp_arr[rows-1][j1][j2] = grid[rows-1][j1]
            else:
                dp_arr[rows-1][j1][j2] = grid[rows-1][j1] + grid[rows-1][j2]

    for i in range(rows - 2, -1, -1):
        import sys
        for j1 in range(cols):
            for j2 in range(cols):
                maxval = -sys.maxsize
                for x1 in [-1, 0, 1]:
                    for x2 in [-1, 0, 1]:
                        collection = 0
                        if j1 == j2:
                            collection = grid[i][j1]
                        else:
                            collection = grid[i][j1] + grid[i][j2]

                        if ((j1 + x1 < 0 or j1 + x1 >= cols) or (j2 + x2 < 0 or j2 + x2 >= cols)):
                            collection = int(-1e8)
                        else:
                            collection = collection + dp_arr[i+1][j1+x1][j2+x2]

                        maxval = max(maxval, collection)
                dp_arr[i][j1][j2] = maxval

    return dp_arr[0][0][cols - 1]

# Define the second function
import sys

def maximumChocolates(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]

    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                dp[n - 1][j1][j2] = grid[n - 1][j1]
            else:
                dp[n - 1][j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

    for i in range(n - 2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = -sys.maxsize
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]

                        if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):
                            ans += int(-1e9)
                        else:
                            ans += dp[i + 1][j1 + di][j2 + dj]

                        maxi = max(ans, maxi)

                dp[i][j1][j2] = maxi

    return dp[0][0][m - 1]

# Test the functions
result1 = cherry_pickup_dp(grid)
result2 = maximumChocolates(grid)

print(result1)
print(result2)

# Check if results are the same
print("Both functions give the same result:", result1 == result2)

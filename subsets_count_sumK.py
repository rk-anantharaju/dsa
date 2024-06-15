
def count_subsets(index, target, arr):
    
    # base cases
    if target == 0: 
        return 1
    
    if index == 0:
        return arr[0] == target
    
    nottake = count_subsets(index-1, target, arr)

    take = 0

    if (arr[index] <= target):
        take = count_subsets(index-1, target-arr[index], arr)

    return take + nottake    
     

def count_subsets_memoization(index,target, arr, dp_arr):
    
    if target == 0:
        return 1

    if index == 0:
        return arr[0] == target
    

    if dp_arr[index][target] != -1:
        return dp_arr[index][target]
    
    nottake = count_subsets_memoization(index-1, target, arr, dp_arr)

    take = 0

    if (arr[index] <= target):
        take = count_subsets_memoization(index-1, target-arr[index], arr, dp_arr)

    dp_arr[index][target] = take + nottake 

    return take + nottake 


def count_subsets_tabulation(target, arr):
    lenght = len(arr)

    dp_arr = [[0 for _ in range(target+1)] for _ in range(lenght)]


    for index in range (lenght):
        dp_arr[index][0] = 1

    if arr[0] <= target:
        dp_arr[0][arr[0]] = 1

    for index in range(lenght):
        for tgt in range(1, target+1):

            nottake = dp_arr[index-1][tgt]
            take = 0
            if arr[index] <= tgt:
                take = dp_arr[index-1][ tgt - arr[index] ]
            
            dp_arr[index][tgt] = take + nottake      
    
    print(dp_arr)
    return dp_arr[lenght-1][target]

for tgt in range (9):
    arr = [1, 2, 2, 3]
    k = tgt

arr= [1,1,1]
k = 2
print (count_subsets(len(arr)-1,k, arr))

dp_arr =  [[-1 for _ in range(k+1)] for _ in range(len(arr))]

print (count_subsets_memoization(len(arr)-1,k, arr, dp_arr))

print (count_subsets_tabulation(k, arr), "\n\n")
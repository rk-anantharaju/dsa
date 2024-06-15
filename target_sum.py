# https://takeuforward.org/data-structure/subset-sum-equal-to-target-dp-14/


#with recursion 
def check_target_sum(index, target, arr):
    length = len(arr)

    # base conditiion - if the target is zero, then we already found the subsequence satisfying the target sum
    if target == 0: 
        return True
    
    if index == 0 :
        return arr[0] == target

    if  arr[index] == target:
        return True
    
    not_take = check_target_sum(index-1, target, arr)
    
    take = False

    if arr[index] < target:
        take = check_target_sum(index-1, target-arr[index], arr)

    return not_take or take   



#with recursion 
def check_target_sum_memoization(index, target, arr, dparr):
    length = len(arr)

    # base conditiion - if the target is zero, then we already found the subsequence satisfying the target sum
    if target == 0: 
        return True
    
    if index == 0 :
        return arr[0] == target

    if  arr[index] == target:
        return True
    
    if dparr[index][target] != -1:
        return dparr[index][target]

    
    not_take = check_target_sum(index-1, target, arr)
    
    take = False

    if arr[index] < target:
        take = check_target_sum(index-1, target-arr[index], arr)
    
    dparr[index][target] = not_take or take
    
    return not_take or take   

#with tabulation 
def check_target_sum_tabulation(index, target, arr):
    dparr = [[ False for x in range(k+1)] for y in range(len(arr))]

    for i in range(index):
        dparr[i][0] = True

   
    if arr[0] <= target:
        dparr[0][arr[0]] = True

    
    for i in range(0, index):
        for t in range(1, target+1):

            not_take = dparr[i-1] [t]
    
            take = False

            if arr[i] <= t:
                take = dparr[i-1][t-arr[i]]        
        
            dparr[i][t] = not_take or take
    
    return dparr[index-1][target]   





arr = [1, 82]
k = 91
print(check_target_sum(len(arr)-1, k, arr))

dparr = [[-1 for x in range(k+1)] for y in range(len(arr))]

print(check_target_sum_memoization(len(arr)-1, k, arr, dparr))

print(check_target_sum_tabulation(len(arr), k, arr))

import timeit

print(timeit.timeit("check_target_sum_tabulation(len(arr), k, arr)", globals=globals()))
print(timeit.timeit("check_target_sum(len(arr)-1, k, arr)", globals=globals()))
print(timeit.timeit("check_target_sum_memoization(len(arr)-1, k, arr, dparr)", globals=globals()))

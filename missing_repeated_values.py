

def findMissingAndRepeatedValues(grid):
    #  size n * n with values in the range [1, n2]. i.e all are sequential numbers 
    flatten_list = sum(grid, [])
    leng =  len(flatten_list)
    
    # diff between the given array sum and sum set values gives the duplicate value 
    given_sum = sum(flatten_list)
    given_set_sum = sum(set(flatten_list))
    duplicate = given_sum - given_set_sum

    # diff between the all #s sum and sum set values gives the missing value
    total_sum =  int((leng*(leng+1))/2) 
    missing = total_sum - given_set_sum

    return [duplicate, missing]




grid = [[1,3],[2,2]]
print(findMissingAndRepeatedValues(grid))

grid = [[9,1,7],[8,9,2],[3,4,6]]
print(findMissingAndRepeatedValues(grid))






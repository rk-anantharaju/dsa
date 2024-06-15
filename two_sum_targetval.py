nums = [2,7,8,15]
target = 18



def two_sum(nums, target):
    read_values = dict()
    
    position = 0
    for val in nums:
        remaining = target - val
        if remaining in read_values:
            return [read_values[remaining], position]
        else:
            read_values[val] = position
        
        position += 1
    
    return []
    
    
print (two_sum(nums, target))    
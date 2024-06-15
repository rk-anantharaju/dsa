nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = set()
    arr_length = len(nums)    
    for i in range(len(nums)):
        
        target = 0 - nums[i]
        
        val_dict = dict()
        
        for j in range(i+1, arr_length):
            # print("nums[j] ", nums[j] )
            remaining = target - nums[j]
            
            if remaining in val_dict:
                values = [nums[i], nums[j], remaining]
                # print(values)
                values.sort()
                # print(values)
                result.add(tuple(values))
                # Dont break here, as there can be multiple combinations
                # break    
            
            val_dict[nums[j]] = j
        
                
            
    # print(result)
    return [list(ii) for ii in result]    


# tj = threeSum(nums)
#print(threeSum(nums))   

def threesum_v2(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            #since the list is sorted, when s < 0, we need to move the left pointer to the right to get a bigger value
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                result.append((nums[i], nums[l], nums[r]))
                '''
                To avoid duplicates, the code skips over duplicate numbers by incrementing l while the next number is the same 
                    (while l < r and nums[l] == nums[l + 1]: l += 1).
                Similarly, it skips over duplicates by decrementing r while the previous number is the same 
                    (while l < r and nums[r] == nums[r - 1]: r -= 1).
                the following two line can enhance performance if there are duplicates in the given array and array is sorted
                '''
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return [list(ii) for ii in result] 

print(threesum_v2(nums))
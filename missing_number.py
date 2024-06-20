'''
https://leetcode.com/problems/missing-number/description/

'''


def missingNumber1(nums) :
    
    # tracking which #s are present in the given array, the position with 0 is the missing #
    data = [0] * (len(nums) +1)

    for num in nums:
        data[num] = data[num] + 1

    for i in range(len(data)):
        if data[i] == 0:
            return i

def missingNumber(nums) :
    leng =  len(nums)
    # diff between the given array sum and sum of all #s 
    return int((leng*(leng+1))/2 - sum(nums)) 
    

nums = [3,0,1]
print(missingNumber(nums))
print(missingNumber1(nums))    

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))
print(missingNumber1(nums))    
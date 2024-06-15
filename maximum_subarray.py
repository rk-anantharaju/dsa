'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_sum_subarray(nums):
    curr_start = 0
    max_start = -1
    max_end = -1
    
    max_sum = float('-inf')
    curr_sum = 0
    
    for i in range (len(nums)):
        
        
        if curr_sum == 0:
            curr_start = i

        curr_sum = curr_sum + nums[i]
        
        if max_sum < curr_sum:
            max_sum = curr_sum
            max_start = curr_start
            max_end = i+1
            
        if curr_sum < 0:
            curr_sum = 0

    print (max_sum)
    print (sum(nums[max_start:max_end]))        
    print (nums[max_start:max_end])     
            

max_sum_subarray(nums)            
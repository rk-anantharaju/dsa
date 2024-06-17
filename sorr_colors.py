'''
https://leetcode.com/problems/sort-colors/description/

https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/

'''

def sort_colors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        # print ("low ", low,  "  mid  ", mid, " high ", high)

        if nums[mid] == 0:
            nums[mid] = nums[low]
            nums[low] = 0
            low += 1
            mid += 1
        elif  nums[mid] == 1:
            mid += 1
        elif  nums[mid] == 2:
            nums[mid] = nums[high] 
            nums[high] =  2
            high -= 1 

        
    print(nums)


# nums = [2,0,2,1,1,0]
nums = [2,0,1]
sort_colors(nums)        
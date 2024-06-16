'''
https://leetcode.com/problems/next-permutation/description/

https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/

'''

from typing import List

def nextGreaterPermutation(nums):
    n = len(nums)

    #track the reversing position, if array is monotonicly increasing, index remains -1
    index = -1
    
    # find the position, where #s start reducing - begin from the last position

    for idx in range(n-2, -1, -1):
        if nums[idx] < nums[idx+1]:
            # print(" nums[idx] ", nums[idx],)
            index = idx
            break

    if index == -1:
        # input is a monoticnally increasing array, we don't have next permutaion, hence reverse it. i.e. smallest one
        return list(reversed(nums))        

    print(nums)
    # given array is monotonic from n-1 till index, find the smallest number, which is > value at the index position and swap it.
    for idx in range(n-1, index, -1):
        if nums[idx] > nums[index]:
            nums[idx], nums[index] = nums[index], nums[idx]
            break
    print(nums)    

    # revere the sting from index till the lastposition
    nums[index+1:] = reversed(nums[index+1:])
    print(nums)

    return nums

nums = [1,2,3]
nums = [5,2,3,2,1,0,0]
nums = [3,2,1]
ans = nextGreaterPermutation(nums)

print("The next permutation is:", ans)
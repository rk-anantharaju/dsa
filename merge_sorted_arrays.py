'''
https://leetcode.com/problems/merge-sorted-array/

https://takeuforward.org/data-structure/merge-two-sorted-arrays-without-extra-space/

'''

def merge(nums1, m, nums2, n):
    if m == 0:
        nums1 = nums2
        return
    
    if n == 0:    
        return
    
    nums1[m:] = nums2

    nums1.sort()
    

def merge_v2(nums1, m, nums2, n):
    
    if m == 0:
        nums1[:] = nums2
        return
    
    if n == 0:    
        return

    idx1 = m-1
    idx2 = n-1
    writer = len(nums1) -1

    while idx2 >= 0  :
        if idx1 >=0 and nums1[idx1] >= nums2[idx2]:
            nums1[writer] = nums1[idx1]
            idx1 -= 1
        else:
            nums1[writer] = nums2[idx2]
            idx2 -= 1

        writer -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge_v2(nums1, m, nums2, n)
print(nums1)
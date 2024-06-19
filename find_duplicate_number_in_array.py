'''
Floyd's Tortoise and Hare Algorithm (Cycle Detection)

Definitions and Assumptions:

    k: Distance from the start of the array to the start of the cycle.
    m: Distance from the start of the cycle to the intersection point within the cycle.
    Cycle Length (C): The number of steps to complete one cycle.
    Steps Taken:
        Slow Pointer: k + m steps when the intersection is found.
        Fast Pointer: 2(k + m) steps when the intersection is found.

Calculation:

    When the pointers meet, the fast pointer has traveled twice the distance of the slow pointer.
    This means 2(k + m) = k + m + nC (where n (some constant) is the number of full cycles completed by the fast pointer)
    Simplifying, we get k + m = nC  i.e k = nC - m (since the fast pointer's extra distance must be a multiple of the cycle length)

    
In the second phase:

    The slow pointer starts at m. 
    When the fast pointer moves K steps, the slow pointer, which starts at m, moves (nC-m) + m steps. 
    This equals K, confirming that the slow pointer completes the cycle as well.

    The slow pointer is initially at m. When the fast pointer moves K steps, the slow pointer which is at m moves (nC-m) + m steps, 
    making slow pointer also completing the cycle.

In a non-cyclic array, eventually, the fast pointer will either:

    Move beyond the bounds of the array, leading to an IndexError, or
    Continuously move to new positions without ever meeting the slow pointer.        

 https://leetcode.com/problems/find-the-duplicate-number/description/

 https://takeuforward.org/data-structure/find-the-duplicate-in-an-array-of-n1-integers/       
'''



def find_duplicate(nums):
    slow = 0
    fast = 0

    while True:

        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    fast = 0

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1,3,4,2,2]
# Output: 2

# nums = [3,1,3,4,2]
# Output: 3

# nums = [3,3,3,3,3]
# Output: 3


print(find_duplicate(nums))
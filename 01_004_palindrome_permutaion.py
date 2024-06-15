#Given a String, check if it is a Permutation of a Palindrome

input_str = "sramars"

# this is efficent way to check if a string is a permutation of a palindrome 
# conunters approach is slower than this approach
def check_permuation_of_palindrome(input_param):
    count_dict = dict()
    
    for ch in input_param:
        if ch in count_dict:
            count_dict[ch] += 1
        else:
            count_dict[ch] = 1
    
    char_counts =  count_dict.values()
    odd_values_count = sum(1 for number in char_counts if number % 2 != 0)
    
    return odd_values_count <= 1
    
from collections import Counter
def check_permuation_of_palindrome2(input_param):
    counters = Counter(input_param)
    
    odd_values_count = sum(1 for number in counters.values() if number % 2 != 0)
    
    
    return odd_values_count <= 1


# print (check_permuation_of_palindrome(input_str))    

import timeit

print(timeit.timeit("check_permuation_of_palindrome(input_str)", globals=globals()))
print(timeit.timeit("check_permuation_of_palindrome2(input_str)", globals=globals()))


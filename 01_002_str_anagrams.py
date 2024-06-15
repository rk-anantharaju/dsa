input1 = 'ASTRONOMER'
input2 = 'MOONSTARER'

# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/

### solutions
'''
1 . Sort the two given strings and compare, if they are equal then they are anagram of each other.
    Time Complexity: O(N * logN), For sorting.
    Auxiliary Space: O(1) as it is using constant extra space

2.  Count the frequency of each character in both the strings and compare the frequency. 
    If the frequency of each character in both the strings is same then they are anagram of each other.
    Time Complexity: O(N), where N is the length of the string.
    Auxiliary Space: O(1) as it is using constant extra space.

    # compare length
    # Create two count arrays and initialize all values as 0	
    # For each character in input strings, increment count in the corresponding count array
    # Compare count arrays

 3.  Using dictionary - Count the frequency of each character from one string and
     use it as reference to compare the frequency of each character in the other string.
     Time Complexity: O(N)
     Auxiliary Space: O(1), Hashmap uses an extra space    

'''

'''Edge cases
    1. input strings are empty
    2. input strings are of different length
    3. case sensitive
    4. input strings are unicode
    5. input strings are of different encoding
    6. white spaces in the input strings
'''
def is_anagram(input_str1, input_str2):
    
    if len(input_str1) != len(input_str2):
        return False
    
    char_dict = dict()
    
    for ch in input_str1:
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1
    
    for ch in input_str2:
        if ch in char_dict:
            char_dict[ch] -= 1
        else:
            return False
    
    if not any(value != 0 for value in char_dict.values()):
        return True
    return False    
    pass
    
    
print (is_anagram(input1, input2))    
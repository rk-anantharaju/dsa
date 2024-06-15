s = "abcabcbb"

s = "bbbbb"
s = "1234567"
s = "aa"
s = "pwwke"
s = "abcde"
def lengthOfLongestSubstring(s):
    # print(s)
    #define left and right pointers
    right_idx = 0
    left_idx = 0
    #current max lenght
    current_max = 0
    #dict to store the visited chars
    visited = dict()
    
    s_length = len(s)
    
    while right_idx < s_length:
        curr_char = s[right_idx]
        print("before ", curr_char, visited, left_idx, right_idx,  current_max)
        
        #check if char is present in the dict
        if curr_char in visited and visited[curr_char] >= left_idx:
             # reset left index in the visited 
            left_idx = visited[curr_char]+1
           
            # update current max length 
            # increment left index, as we found a duplicate char at left_idx
            
        current_max = max (current_max, right_idx - left_idx +1)   
            
            # left_idx = visited[curr_char]+1
        visited[curr_char] = right_idx
 
        right_idx += 1
        print("after ", curr_char, visited, left_idx, right_idx,  current_max)
    print(current_max)        
    return current_max

print(lengthOfLongestSubstring(s))
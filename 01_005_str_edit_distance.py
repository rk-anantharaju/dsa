import numpy as np

# Driver code
str1 = "rmz"
str2 = "rmza"

n = len(str1)
m = len(str2)
dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

#using dynamic programming 
def is_edit_distance_one(s1, s2):
    n = len(s1)
    m = len(s2)
     
    if abs(n - m) > 1:
        return False
     
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
     
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert
                                   dp[i-1][j],      # Remove
                                   dp[i-1][j-1])    # Replace
     
    return dp[n][m] == 1

print("using dynamic programming - ", is_edit_distance_one(str1, str2))



def is_one_edit(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    
    if abs(str1_len - str2_len) > 1:
        return False
    
    #loop over smaller string, compare each character
    #track difference if the characters are mismatched
    #return false if another difference is observed
    idx1 = 0
    idx2 = 0
    diff_fount = 0
    while idx1 < str1_len and idx2 < str2_len:
        if str1[idx1] != str2[idx2]:
            
            if diff_fount > 0:
                print ("111111 ", idx1, idx2)
                return False
            
            diff_fount = 1

            if str1_len > str2_len:
                idx1 += 1
            elif str1_len < str2_len:
                idx2 += 1
            else:
                idx1 += 1
                idx2 += 1
            
        else:
            idx1 += 1
            idx2 += 1
    
    if idx1 < str1_len or idx2 < str2_len:
        diff_fount += 1
        

    return diff_fount == 1
        
    

print (is_one_edit(str1, str2))        
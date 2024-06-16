
'''
https://leetcode.com/problems/pascals-triangle/description/

https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/

'''
def generate_v1(numRows):
    output = []
    for i in range(1, numRows+1):
        row = [1]
        ans = 1
        for j in range(1, i):
            ans = int((ans *(i-j))/j)
            row.append(ans)
        output.append(row)
    return output   

def generate(numRows):
    output = []
    for i in range(1, numRows+1):
        row = [1]*i
        
        if i<=2:
            output.append(row)
            continue
        
        for j in range(1, i-1):
            # print(row[j])
            row[j] = output [i-2][j-1] + output [i-2][j]
        
        output.append(row)
    return output  


rows = 5
import timeit

print(timeit.timeit("generate(rows)", globals=globals()))
print(timeit.timeit("generate_v1(rows)", globals=globals()))

'''
https://leetcode.com/problems/rotate-image/description/

https://takeuforward.org/data-structure/rotate-image-by-90-degree/

'''

def rotate(matrix):
    size = len(matrix)

    # for i  in range(size):
    #     for j in range(i+1):
    #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
    matrix[:]=[list(row) for row in zip(*matrix)]        

    for i  in range(size):
        matrix[i].reverse()    

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in matrix]))

rotate(matrix)
print("\n")
print('\n'.join(['  '.join([str(cell) for cell in rowx]) for rowx in matrix]))



#zip sample 0
'''
zip() function in conjunction with the asterisk * operator to unpack iterables. 
This is often used to “unzip” a list of tuples.
'''

pairs = [("a", 1, 10),
          ("b", 2, 20), 
          ("c", 3, 30)]

letters, numbers, tens = zip(*pairs)
print(letters)
print(numbers)
print(tens)
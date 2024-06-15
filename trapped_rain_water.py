'''

https://www.geeksforgeeks.org/trapping-rain-water/
https://www.enjoyalgorithms.com/blog/trapping-rain-water

monotonic stack
https://www.youtube.com/watch?v=ZI2z5pq0TqA
https://www.youtube.com/watch?v=UMFKP9cTDtI

'''
heights = [0,1,0,2,1,0,1,3,2,1,2,1]

# heights = [5,1,2]

# https://www.youtube.com/watch?v=ZI2z5pq0TqA
# using two pointer approach, find the min height of the left and right walls, which guarantees the water trapping. 
# even if other side has  a bigger wall  the water trapped is limited by the smaller wall
def trapped_rain_water(height):
    left_index = 0
    right_index = len(height) -1

    left_max = height[left_index]
    right_max = height[right_index]

    total_water = 0
    
    while left_index < right_index:
        if left_max < right_max:
            left_index += 1
            left_max = max (left_max, height[left_index])
            total_water += left_max  - height[left_index]
            
        else:
            right_index -= 1
            right_max = max(right_max, height[right_index])
            total_water += right_max  - height[right_index]
    return total_water
    

#using monotonic stack
#https://cdn-images-1.medium.com/max/600/1*Y2ROlVvW5FUJyrhxgRfstw.png

def trapped_water_stack(height):
    
    stack = []
    trapped_rain_water = 0
    for i in range(len(height)):
        while len(stack) > 0 and height[i] > height[stack[-1]]:
            
            top = stack.pop()
            if len(stack) == 0:
                break
            # compute height - find min of the two side walls and minus the current wall height
            left_height = height[stack[-1]]
            right_height = height[i]
            wall_height = min (left_height,right_height ) - height[top]
            
            # compute width 
            water_width = i - stack[-1] - 1
            
            # compuate trapped_rain_water
            
            trapped_rain_water += wall_height * water_width
        
        stack.append(i)
    return trapped_rain_water
    
        



import timeit

print("two pointer ", timeit.timeit("trapped_rain_water(heights)", globals=globals()))
print("stack based ", timeit.timeit("trapped_water_stack(heights)", globals=globals()))

# print(trapped_rain_water(heights))
# print(trapped_water_stack(heights))
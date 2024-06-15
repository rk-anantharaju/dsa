points = [[10, 40, 70],
          [20, 50, 80],
          [30, 60, 90]]

# points =    [[18, 11, 19], [4, 13, 7], [1, 8, 13]]

# points = [[10, 50, 1], [5, 100, 11]]

# using recursion approach  + memoization
def ninja_training(day, prev_task, points, data_store):

    # if data is already present in data_store, return that, instead of calculating again
    # this is benficial when we have overlapping subproblems and memoization helps to avoid recalculating the same subproblem
    if data_store[day][prev_task] != -1:
        # print ("data present for day, prev_task" , day, prev_task, data_store)
        return data_store[day][prev_task]
        
    task = len(points[0])
    maxp = 0
    # for first day, we can choose the task with max points
    if day == 0:
        for i in range(task):
            if i != prev_task:
                maxp = max(maxp, points[day][i])
    
    else:
        # for other days chose the task give max points, when combined with the points from previous day
        # which ever combination gives max points, choose that
        for i in range(task):
            if i != prev_task:
                maxp = max (maxp, points[day][i] + ninja_training(day-1, i, points, data_store))
    
        
    data_store[day][prev_task] = maxp
    print ("day, prev_task" , day, prev_task, data_store)    
    return data_store[day][prev_task]

#using tabulation approach
def ninja_training_tabulation(points):
    data_store = [[ 0 for i in range(task+1)] for i in range(days)]
    
    for day in range(0, len(points)):
        for last_task in range(task+1):
            data_store[day][last_task] = 0 
            tasks = len(points[0])
            maxp = 0
            # for first day, we can choose the task with max points
            if day == 0:
                for i in range(task):
                    if i != last_task:
                        maxp = max(maxp, points[day][i])
                        
            
            else:
                # for other days chose the task give max points, when combined with the points from previous day
                # which ever combination gives max points, choose that
                for i in range(task):
                    if i != last_task:
                        maxp = max (maxp, points[day][i] + data_store[day-1][i])
                                    
            data_store[day][last_task] = maxp
                
            
    print(data_store)    
    return data_store[day][-1]    

    
days = len(points)
task = len(points[0])

data_store = [[ -1 for i in range(task+1)] for i in range(days)]

# print(data_store)    
# print(points)

#trigger the recursive function with last day and assuming no task is done on that day    
print(ninja_training(days - 1, task, points, data_store))
print(ninja_training_tabulation( points))   
# print(ninjaTraining(days, points)) 
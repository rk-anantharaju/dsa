'''
https://leetcode.com/problems/merge-intervals/description/

https://takeuforward.org/data-structure/merge-overlapping-sub-intervals/

'''
def merge(intervals):

    merged_intervals = []
    intervals.sort()
    # print(intervals)

    for interval in intervals:
        # check if the first elment of current interval, is less than the currently computed range's limit
        # if its within the range, expand current range, otherwise create a new range with the new interval
        if not merged_intervals or interval[0] > merged_intervals[-1][1]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1][1] =  max(interval[1], merged_intervals[-1][1])   

    return merged_intervals




intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

# intervals = [[1,4],[4,5]]
# Output: [[1,5]]

print(intervals)
print(merge(intervals))
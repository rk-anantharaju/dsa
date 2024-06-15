nums = [1, 9, 4]
# nums = [2, 1, 4, 9]

# https://takeuforward.org/data-structure/maximum-sum-of-non-adjacent-elements-dp-5/

def max_non_adjacent_sum(nums):
    # print(nums)
    length = len(nums)
    data_arr = [-1]*length
    onestep = 0
    twostep = 0 

    for i in range(length):
        if i == 0:
            data_arr[i] = nums[i]
            continue

        if i == 1:
            data_arr[i] = max(nums[i], nums[i-1])
            continue
        
        onestep = data_arr[i-1] 

        if i > 1:
            twostep = data_arr[i-2] + nums[i]

        data_arr[i] = max(onestep, twostep)

        # print(data_arr)    

    return data_arr[-1]


nums = [8, 15, 120, 100, 10, 4]
# print(max_non_adjacent_sum(nums))

print(nums)
print(nums[1:])
print(nums[:len(nums)-1])
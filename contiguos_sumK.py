# https://takeuforward.org/arrays/count-subarray-sum-equals-k/
# https://www.youtube.com/watch?v=xvNwoz-ufXA
# https://leetcode.com/problems/subarray-sum-equals-k/
def subarray_sum(nums, k: int) -> int:
    sum = 0
    dic = {0:1}
    count = 0
    length = len(nums)
    
    for num in nums:
        
        sum += num
        remain = sum - k
        
        if remain in dic:
            count += dic[remain]
        
        dic[sum] = dic.get(sum, 0) + 1    

    return count    


nums = [1,1,1]
k = 3

print(subarray_sum(nums, k))
# 45 minutes, didn't manage to come up with the working solution
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        # [2,3,1,2,4,3], s = 7
        # i = 0, j = 0
        # 2, 3, 1, 2
        # i = 0, j = 3
        # can't move i
        # move j
        # j = 4, sum = 12
        # move i: i = 1, sum = 12 - arr[0] = 10
        # 10 - arr[1] = 7, i  = 2
        # i = 2, j = 4
        # can't move i, move j:
        # i = 2, j = 5, sum = 10
        # move i. 10 - arr[2] = 10 - 1 = 9, i = 3, j = 5
        # 9 - arr[3] = 7, i = 4, j = 5
        # 7 - arr[4] = 3, stop moving i, try to move j, j > len(arr), return arr[i:j + 1]
        
        
        i, j, min_length, subarray_sum, cur_len = 0, 0, 0, 0, 0
        if len(nums) == 0:
            return 0
        for j in range(len(nums)):
        #while j < len(nums):
            while subarray_sum < s:
                subarray_sum += nums[j]
                j += 1  
                cur_len = j - i + 1
            else: # if sumarray_sum >= s
                while subarray_sum - nums[i] >= s:
                    subarray_sum -= nums[i]
                    i += 1
                
            if j - i + 1 < cur_len:
                min_length = j - i + 1
        if subarray_sum < s:
            return 0
        else:
            return min_length
            
            
    '''
    [2, 3, 1, 4, 3, 2]
    i = 0, j = 0, sum = 2, len = 
    i = 0, j = 1, sum = 5, len = 
    i = 0, j = 2, sum = 6, len = 
    i = 0, j = 3, sum = 10, len =
    # else
    len = 3 - 0 + 1 = 4
    10 - nums[0] = 10 - 2 = 8
    i = 1, j = 3, len = 3, sum = 8
    8 - nums[i] = 8 - 3 = 5, don't move, don't update
    # if
    i = 1, j = 4, sum = 11, len = 4
    # else
    11 - nums[i] = 8,
    i = 2, j = 4, sum = 8, len = 3,
    8 - nums[i] = 7
    i = 3, j = 4, sum = 7
     
    '''
          

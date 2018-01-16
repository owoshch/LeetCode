class Solution:
    def moveZeroes(self, nums):
        last_non_zero_found_at = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                #swap
                temp = nums[last_non_zero_found_at]
                nums[last_non_zero_found_at] = nums[cur]
                nums[cur] = temp
                last_non_zero_found_at += 1
        return   

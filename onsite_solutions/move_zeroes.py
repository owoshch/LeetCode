class Solution:    
    def moveZeroes(self, arr):
        last_zero_index = 0
        non_zero_element_index = 0
        while non_zero_element_index < len(arr):
            if arr[non_zero_element_index] == 0:
                non_zero_element_index += 1
            else:
                #swap non-zero element and last zero element
                temp = arr[non_zero_element_index]
                #print (non_zero_element_index)
                arr[non_zero_element_index] = arr[last_zero_index]
                arr[last_zero_index] = temp
                non_zero_element_index += 1
                last_zero_index += 1
        return
        

# first 15 minutes
# yes, I feel really awful
# I'll start over this assignment

class Solution:
    def compute_sum(self, a, b, add_value):
        # returns (int, bool)
        return ((int(a) + int(b) + int(add_value)) % 2, \
                        int(a) + int(b) + add_value > 1)
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        add_value = False
        b = ("{0}" + b).format("0" * (len(a) - len(b)))
        print (a, b)
        for first_number, second_number in zip(a[::-1], b[::-1]):
            new_number, add_value = self.compute_sum(first_number, second_number, add_value)
            result += str(new_number)
            print (new_number, result)
        if add_value:
            result += "1"
        result = result[::-1]
        return result
        
        
        # a b sum(a, b) 
        # 0 0 0
        # 0 1 1
        # 1 0 1
        # 1 1 10
        
        # 111111
        # .   10
        # ------
        #1000001
        
        
            
        
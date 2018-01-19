# result after 30 minutes
# comments before the actual code would be said to the interviewer

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        # iterate through, push opening parentheses into stack
        # pop stack while facing closing parentheses
        # ()) :
        # (
        # ()
        # ()) i don't have opening parentheses : a[:last_index] without last opening one + )
        # .                                      a[:last_index]
        
        # ): stack is empty, just have to delete this one
        # (: reached end with one opening bracket - remove
        
        # iterate through the string, keep track of index
        # add opening parentheses to the stack
        # () - add correct to the output [()]
        # () - add correct to the output
        # ) - need to remove this, or any other closing parentheses from the output
        # ()
        
        # ( - remove it.
        brackets_stack = []
        output = [""]
        for i, symbol in enumerate(s):
            if symbol == "(":
                if len(stack):
                    brackets_stack.append((symbol, i))
            elif symbol == ")":
                if len(stack): #if stack is not empty
                    output = [x + s[brackets_stack.pop()[1]:i+1] for x in output]
                else: #if stack is empty
                    for string in output:
                        for...
                        
        #gave up, decided to check the solution
                    
                    
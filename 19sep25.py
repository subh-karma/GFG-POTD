class Solution:
    def minParentheses(self, s):
        # code here
        l = 0 # number of unclosed left parentheses
        total = 0
        for i in s:
            if i == ")" and l==0: # unmatched closing brackets
                total+=1
            elif i == ")": # matching bracket found
                l -= 1
            else:
                l+=1
        
        return total +l
        # code here
        
        

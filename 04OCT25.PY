class Solution:
    def findExpr(self, s, target):
        res = []
        
        def backtrack(index, expr, value, prev):
            # index: current position in string
            # expr: expression built so far
            # value: evaluated value so far
            # prev: last operand (for handling '*')
            
            if index == len(s):
                if value == target:
                    res.append(expr)
                return
            
            for i in range(index, len(s)):
                # Avoid numbers with leading zeros
                if i > index and s[index] == '0':
                    break
                    
                num_str = s[index:i+1]
                num = int(num_str)
                
                if index == 0:
                    # First number (no operator before it)
                    backtrack(i+1, num_str, num, num)
                else:
                    # Addition
                    backtrack(i+1, expr + "+" + num_str, value + num, num)
                    # Subtraction
                    backtrack(i+1, expr + "-" + num_str, value - num, -num)
                    # Multiplication
                    backtrack(i+1, expr + "*" + num_str, value - prev + prev * num, prev * num)
        
        backtrack(0, "", 0, 0)
        res.sort()  # lexicographically smallest order
        return res
        # code here
        
        

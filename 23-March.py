#User function Template for python3
class Solution:
    def countWays(self, digits):
        # Code here
        
        if digits[0] == '0':
            return 0
        
        length = len(digits)
        prev1 = 1
        prev2 = 1
        for index in range(2, length+1):
            count = 0
            if digits[index-1] > '0':
                count = prev1
            if digits[index-2] == '1' or (digits[index-2] == '2' and digits[index-1] < '7' ):
                count += prev2
            prev2 = prev1
            prev1 = count
        return prev1

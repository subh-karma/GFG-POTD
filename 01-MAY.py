#User function Template for python3
class Solution:

    def nthRowOfPascalTriangle(self, n):
        
        r = n - 1
        row = [1]

        for k in range(1, n):
            prev = row[-1]                   
            num   = r - (k - 1)               
            den   = k                         
            next_val = prev * num // den     
            row.append(next_val)
        return row

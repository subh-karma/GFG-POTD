class Solution:
    def binstr(self, n):
        # code here
        res= []
        for i in range(2**n):
            
            res.append(format(i, f'0{n}b'))
        return res

        # code here
        

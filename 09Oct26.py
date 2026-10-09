class Solution:
    def minOperation(self, n):
        # code here
        # let us try top to down approach 
        # consider number of operations - 0
        op=0
        while n>0:
            if n%2==0:# keep dividing unless its 0 and divisible by 2
                n//=2
            else:# its odd so subtract 1
                n-=1
            op+=1# count operation
        return op 
        

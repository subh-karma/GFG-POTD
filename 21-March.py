class Solution:  
    def findMaxSum(self,arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        prev = 0
        sprev = 0
        for num in arr:
            current = max(prev, sprev + num)
            sprev = prev
            prev = current
        return prev
        

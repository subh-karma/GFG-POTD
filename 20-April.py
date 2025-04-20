class Solution:
    def findDuplicate(self, arr):
        #code here
        n = len(arr)
        for index in range(n):
            
            target_i = arr[index]%n
            
            arr[target_i]+= n
        
        
        for index in range(n):
            
            repetition = arr[index]//n
            
            if repetition > 1:
                return index
        
        return -1

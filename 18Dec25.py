class Solution:
    def sortIt(self, arr):
        arr.sort(key=lambda x:-x if x&1 else x)
        # code here
        
    

class Solution:
    def minSubsets(self, arr):
        s = set(arr)
        return sum(x - 1 not in s for x in s)
        #code here
        

class Solution:
     def countMinOperations(self, arr):
        return sum(a.bit_count() for a in arr) + max(a.bit_length() for a in arr) - 1
        # code here
        

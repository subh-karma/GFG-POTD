
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        a=set(a)
        b=set(b)
        return len(a.union(b))

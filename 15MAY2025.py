import math
class Solution:
    def solve(self,arr,x):
        return sum(math.ceil(item/x) for item in arr)
    
    def smallestDivisor(self, arr, k):
        l,h=1,max(arr)
        while l<=h:
            mid=(l+h)//2
            if self.solve(arr,mid)>k:
                l=mid+1
            else:
                h=mid-1
        return l
        # Code here

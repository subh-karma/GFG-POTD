class Solution:
     def kthMissing(self, arr, k):
        # code here
        def missing(arr, k):
            lo, hi = 0, len(arr)
            while lo < hi:
                mi = lo+(hi-lo)//2
                if arr[mi] - (mi+1) < k:
                    lo = mi+1
                else:
                    hi = mi
            return lo
            
        
        n = missing(arr, k)
        return n+k
        # code here
        

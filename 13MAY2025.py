#User function Template for python3

class Solution:
    def kokoEat(self,arr,k):
        # Code here
        l, r = 1, max(arr)
        ans =r
        while l<=r:
            mid =l + (r-l)//2
            count = 0 
            for i in arr:
                quo, rem = i//mid, i%mid
                if rem:
                    count += 1
                count += quo
            if count <= k:
                ans = min(ans, mid)
                r = mid-1
            else:
                l = mid+1
        return ans 


        # Code here

class Solution:
    def maxPeopleDefeated(self, p):
        # code here
        l=1
        h=p
        ans = 1
        while l<=h:
            mid = h-(h-l)//2
            if mid*(mid+1)*(2*mid+1)//6<=p:
                ans = mid
                l=mid+1
            else:
                h=mid-1
        return ans
        # code here
        

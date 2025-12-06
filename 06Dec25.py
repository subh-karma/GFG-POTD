
class Solution:
    def maximumAmount(self, arr):
        def fun(a,s,e,f,dp):
            if s>e:
                return 0
            if dp[s][e]!=-1:
                return dp[s][e]
            if f:
                a1=fun(a,s+1,e,0,dp)+a[s]
                a2=fun(a,s,e-1,0,dp)+a[e]
                ans=max(a1,a2)
            else:
                a1=fun(a,s+1,e,1,dp)-a[s]
                a2=fun(a,s,e-1,1,dp)-a[e]
                ans=min(a1,a2)
            dp[s][e]=ans
            return ans
            
            
        n=len(arr)
        s=sum(arr)
        dp=[[-1 for j in range(n)] for i in range(n)]
        a = fun(arr,0,n-1,1,dp)
        a += (s-a)//2
        return a

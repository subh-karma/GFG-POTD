class Solution:
    def isSubsetSum (self, arr, sum):
        def solve(s,ind):
            if s==0:
                return True;
            if ind>=len(arr):
                return False;
            cur_status=False
            if dp[ind][s]!=-1:
                return dp[ind][s];
            if arr[ind]<=s:
                cur_status=cur_status or solve(s-arr[ind],ind+1);
            cur_status=cur_status or solve(s,ind+1);
            dp[ind][s]= cur_status;
            return cur_status
            
        dp=[[-1]*(sum+1) for i in range(len(arr)+1)]
        ans=solve(sum,0);
        return ans;

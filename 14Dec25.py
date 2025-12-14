class Solution:
    def prefixSum2D(self, mat, queries):
        # code here 
        m, n = len(mat), len(mat[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for r in range(m):
            for c in range(n):
                dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1] - dp[r][c] + mat[r][c]
        
        ans = []
        for r1, c1, r2, c2 in queries:
            v = dp[r2+1][c2+1] - dp[r2+1][c1] - dp[r1][c2+1] + dp[r1][c1]
            ans.append(v)
        return ans

    
 


class Solution:
    def minCost(self, keys, freq):
        # code here
        from itertools import accumulate
        n = len(keys)
        dp = [[float('inf') for _ in freq] for _ in freq]
        pre_sum = list(accumulate(freq, initial=0))
        # dp[i][j] means the minimum cost of from i to j inclusive
        # key point: any key will contribute freq[i] to the cost at each level. 
        # dp[i][j] = sum(freq[i:j+1]) + dp[i][k-1] + dp[k+1][j] for k in [i:j+1]
        for i in range(n-1, -1, -1):
            for j in range(i, n): 
                c = pre_sum[j+1] - pre_sum[i]    # any key will contribute to this level
                cost = 0
                for k in range(i, j+1): # choose the root in this segment
                    cost = c
                    if k > i:
                        cost += dp[i][k-1]
                    if k < j:
                        cost += dp[k+1][j]
                    dp[i][j] = min(dp[i][j], cost)
        return dp[0][n-1]
        # code here
        

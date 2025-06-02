class Solution:
    def uniquePaths(self, grid):
        n, m = len(grid), len(grid[0])
        if grid[0][0] or grid[-1][-1]:
            return 0
        dp = [0] * m
        for col in range(m):
            if grid[0][col]:
                break
            dp[col] = 1
        for row in range(1, n):
            if grid[row][0]:
                dp[0] = 0
            for col in range(1, m):
                if grid[row][col]:
                    dp[col] = 0
                else:
                    dp[col] += dp[col - 1]
        return dp[-1]
